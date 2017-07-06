#!powershell
# This file is part of Ansible
#
# Copyright 2015, Peter Mounce <public@neverrunwithscissors.com>
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

$ErrorActionPreference = "Stop"

# WANT_JSON
# POWERSHELL_COMMON

# temporary fix to keep this module working in 2.0. Needs parameter validation fixes to work in future versions
Set-StrictMode -Off

$params = Parse-Args $args;
$result = New-Object PSObject;
Set-Attr $result "changed" $false;

If ($params.name)
{
    $package = $params.name
}
Else
{
    Fail-Json $result "missing required argument: name"
}

Function Find-Command
{
    [CmdletBinding()]
    param(
      [Parameter(Mandatory=$true, Position=0)] [string] $command
    )
    $installed = get-command $command -erroraction Ignore
    write-verbose "$installed"
    if ($installed.length -gt 0)
    {
        return $installed[0]
    }
    return $null
}

Function Find-WebPiCmd
{
    [CmdletBinding()]
    param()
    $p = Find-Command "webpicmd.exe"
    if ($p -ne $null)
    {
        return $p
    }
    $a = Find-Command "c:\programdata\chocolatey\bin\webpicmd.exe"
    if ($a -ne $null)
    {
        return $a
    }
    Throw "webpicmd.exe is not installed. It must be installed (use chocolatey)"
}

Function Test-IsInstalledFromWebPI
{
    [CmdletBinding()]

    param(
        [Parameter(Mandatory=$true, Position=0)]
        [string]$package
    )

    $cmd = "$executable /list /listoption:installed"
    $results = invoke-expression $cmd

    if ($LastExitCode -ne 0)
    {
        Set-Attr $result "webpicmd_error_cmd" $cmd
        Set-Attr $result "webpicmd_error_log" "$results"

        Throw "Error checking installation status for $package"
    }
    Write-Verbose "$results"

    $matches = $results | select-string -pattern "^$package\s+"
    return $matches.length -gt 0
}

Function Install-WithWebPICmd
{
    [CmdletBinding()]

    param(
        [Parameter(Mandatory=$true, Position=0)]
        [string]$package
    )

    $cmd = "$executable /install /products:$package /accepteula /suppressreboot"

    $results = invoke-expression $cmd

    if ($LastExitCode -ne 0)
    {
        Set-Attr $result "webpicmd_error_cmd" $cmd
        Set-Attr $result "webpicmd_error_log" "$results"
        Throw "Error installing $package"
    }

    write-verbose "$results"
    $success = $results | select-string -pattern "Install of Products: SUCCESS"
    if ($success.length -gt 0)
    {
        $result.changed = $true
    }
}

Try
{
    $script:executable = Find-WebPiCmd
    if ((Test-IsInstalledFromWebPI -package $package) -eq $false)
    {
        Install-WithWebPICmd -package $package
    }

    Exit-Json $result;
}
Catch
{
     Fail-Json $result $_.Exception.Message
}
