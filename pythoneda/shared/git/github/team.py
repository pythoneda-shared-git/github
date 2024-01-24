# vim: set fileencoding=utf-8
"""
pythoneda/shared/git/github/team.py

This file defines the Team class.

Copyright (C) 2024-today rydnr's pythoneda-shared-git/github

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import aiohttp
import asyncio
from pythoneda.shared import BaseObject
from typing import List


class Team(BaseObject):
    """
    Interacts with the /orgs/[org]/teams endpoint of github API.

    Class name: Repository

    Responsibilities:
        - Know how to use the github API to manage organization teams.

    Collaborators:
        - None
    """

    def __init__(self, token: str):
        """
        Creates a new Team instance.
        """
        super().__init__()
        self._token = token

    @property
    def token(self) -> str:
        """
        Retrieves the github token.
        :return: Such token.
        :rtype: str
        """
        return self._token

    async def list(self, org: str):
        """
        Retrieves the github teams.
        :param org: The organization name.
        :type org: str
        :return: The list of teams.
        :rtype: List
        """
        async with aiohttp.ClientSession() as session:
            headers = {"Authorization": f"token {self.token}"}
            url = f"https://api.github.com/orgs/{org}/teams"
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    return (
                        await response.json()
                    )  # This will contain the team information
                else:
                    return f"Error: {response.status}, {await response.text()}"


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
