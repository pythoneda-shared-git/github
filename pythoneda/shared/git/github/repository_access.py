# vim: set fileencoding=utf-8
"""
pythoneda/shared/git/github/repository_access.py

This file defines the RepositoryAccess class.

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
import json
from pythoneda.shared import attribute, BaseObject, sensitive
from .repository import Repository
from typing import Dict, Union


class RepositoryAccess(BaseObject):
    """
    Interacts with the /orgs/[org]/repos endpoint of github API.

    Class name: RepositoryAccess

    Responsibilities:
        - Know how to use the github API to access repositories.

    Collaborators:
        - None
    """

    def __init__(self, token: str):
        """
        Creates a new RepositoryAccess instance.
        :param token: The Github token.
        :type token: str
        """
        super().__init__()
        self._token = token

    @property
    @attribute
    @sensitive
    def token(self) -> str:
        """
        Retrieves the github token.
        :return: Such token.
        :rtype: str
        """
        return self._token

    async def fetch(self, org: str, name: str) -> Repository:
        """
        Retrieves a Github repository.
        :param org: The name of the organization.
        :type org: str
        :param name: The name of the repository.
        :type name: str
        :return: The repository instance.
        :rtype: pythoneda.shared.git.github.Repository
        """
        async with aiohttp.ClientSession() as session:
            headers = {
                "Authorization": f"token {self.token.get()}",
                "Content-Type": "application/json",
            }
            url = f"https://api.github.com/repos/{org}/{name}"

            result = None

            async with session.get(url, headers=headers) as response:
                json_response = await response.json()
                bad_credentials = (
                    json_response.get("message", None) == "Bad credentials"
                )
                # print(json_response)
                if response.status in [200, 201] and not bad_credentials:
                    result = Repository(
                        org,
                        name,
                        json_response.get("description", None),
                        json_response.get("homepage", None),
                        json_response.get("private", False),
                        json_response.get("visibility", False),
                        json_response.get("has_issues", False),
                        json_response.get("has_wiki", False),
                        json_response.get("has_downloads", False),
                        json_response.get("has_projects", False),
                        json_response.get("team_id", None),
                        json_response.get("auto_init", None),
                        json_response.get("license_template", None),
                        json_response.get("gitignore_template", None),
                        json_response.get("allow_squash_merge", False),
                        json_response.get("allow_merge_commit", False),
                        json_response.get("allow_rebase_merge", False),
                        json_response.get("allow_auto_merge", False),
                        json_response.get("delete_branch_on_merge", None),
                        json_response.get("use_squash_pr_title_as_default", None),
                        json_response.get("squash_merge_commit_title", None),
                        json_response.get("squash_merge_commit_message", None),
                        json_response.get("merge_commit_title", None),
                        json_response.get("merge_commit_message", None),
                        json_response.get("custom_properties", {}),
                    )

            return result

    async def create(
        self,
        org: str,
        name: str,
        description: str = "",
        homepage: str = "",
        private: bool = False,
        visibility: str = "public",
        hasIssues: bool = True,
        hasWiki: bool = True,
        hasDownloads: bool = True,
        hasProjects: bool = True,
        teamId: Union[int, None] = None,
        autoInit: Union[bool, None] = True,
        licenseTemplate: Union[str, None] = "gpl-3.0",
        gitignoreTemplate: Union[str, None] = "",
        allowSquashMerge: Union[bool, None] = True,
        allowMergeCommit: Union[bool, None] = True,
        allowRebaseMerge: Union[bool, None] = True,
        allowAutoMerge: Union[bool, None] = True,
        deleteBranchOnMerge: Union[bool, None] = True,
        useSquashPrTitleAsDefault: Union[bool, None] = True,
        squashMergeCommitTitle: Union[str, None] = "",
        squashMergeCommitMessage: Union[str, None] = "",
        mergeCommitTitle: Union[str, None] = "",
        mergeCommitMessage: Union[str, None] = "",
        customProperties: Union[Dict[str, str], None] = "",
    ) -> Repository:
        """
        Creates a new repository.
        :param org: The name of the organization.
        :type org: str
        :param name: The name of the repository.
        :type name: str
        :param description: A short description of the repository.
        :type description: str
        :param homepage: A URL with more information about the repository.
        :type homepage: str
        :param private: Whether the repository is private.
        :type private: bool
        :param visibility: The visibility of the repository.
        :type visibility: Either "public" or "private".
        :param hasIssues: Either true to enable issues for this repository or false to disable them.
        :type hasIssues: bool
        :param hasProjects: Either true to enable projects for this repository or false to disable them. Note: If you're creating a repository in an organization that has disabled repository projects, the default is false, and if you pass true, the API returns an error.
        :type hasProjects: bool
        :param hasWiki: Either true to enable the wiki for this repository or false to disable it.
        :type hasWiki: bool
        :param hasDownloads: Whether downloads are enabled.
        :type hasDownloads: bool
        :param isTemplate: Either true to make this repo available as a template repository or false to prevent it.
        :type isTemplate: bool
        :param teamId: The id of the team that will be granted access to this repository. This is only valid when creating a repository in an organization.
        :type teamId: int
        :param autoInit: Pass true to create an initial commit with empty README.
        :type autoInit: bool
        :param licenseTemplate: Choose an open source license template that best suits your needs, and then use the license keyword as the license_template string. For example, "mit" or "mpl-2.0".
        :type licenseTemplate: str
        :param gitignoreTemplate: Desired language or platform .gitignore template to apply. Use the name of the template without the extension. For example, "Haskell".
        :type gitignoreTemplate: str
        :param allowSquashMerge: Either true to allow squash-merging pull requests, or false to prevent squash-merging.
        :type allowSquashMerge: bool
        :param allowMergeCommit: Either true to allow merging pull requests with a merge commit, or false to prevent merging pull requests with merge commits.
        :type allowMergeCommit: bool
        :param allowRebaseMerge: Either true to allow rebase-merging pull requests, or false to prevent rebase-merging.
        :type allowRebaseMerge: bool
        :param allowAutoMerge: Either true to allow auto-merge on pull requests, or false to disallow auto-merge.
        :type allowAutoMerge: bool
        :param deleteBranchOnMerge: Either true to allow automatically deleting head branches when pull requests are merged, or false to prevent automatic deletion. The authenticated user must be an organization owner to set this property to true.
        :type deleteBranchOnMerge: bool
        :param useSquashPrTitleAsDefault: Either true to allow squash-merge commits to use pull request title, or false to use commit message. **This property has been deprecated. Please use squash_merge_commit_title instead.
        :type useSquashPrTitleAsDefault: bool
        :param squashMergeCommitTitle: The default value for a squash merge commit title: PR_TITLE - default to the pull request's title; COMMIT_OR_PR_TITLE - default to the commit's title (if only one commit) or the pull request's title (when more than one commit).
        :type squashMergeCommitTitle: str
        :param squashMergeCommitMessage: The default value for a squash merge commit message: PR_BODY - default to the pull request's body; COMMIT_MESSAGES - default to the branch's commit messages; BLANK - default to a blank commit message.
        :type squashMergeCommitMessage: str
        :param mergeCommitTitle: The default value for a merge commit title: PR_TITLE - default to the pull request's title; MERGE_MESSAGE - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name).
        :type mergeCommitTitle: str
        :param mergeCommitMessage: The default value for a merge commit message: PR_TITLE - default to the pull request's title; PR_BODY - default to the pull request's body; BLANK - default to a blank commit message.
        :type mergeCommitMessage: str
        :param customProperties: The custom properties for the new repository. The keys are the custom property names, and the values are the corresponding custom property values.
        :type customProperties: Dict[str,str]
        :return: The repository instance.
        :rtype: pythoneda.shared.git.github.Repository
        """
        async with aiohttp.ClientSession() as session:
            headers = {
                "Authorization": f"token {self.token.get()}",
                "Content-Type": "application/json",
            }
            url = f"https://api.github.com/orgs/{org}/repos"
            data = {
                "name": name,
                "description": description,
                "private": private,
                "visibility": visibility,
                "hasIssues": hasIssues,
                "hasWiki": hasWiki,
                "hasDownloads": hasDownloads,
                "hasProjects": hasProjects,
                "teamId": teamId,
                "autoInit": autoInit,
                "licenseTemplate": licenseTemplate,
                "gitignoreTemplate": gitignoreTemplate,
                "allowSquashMerge": allowSquashMerge,
                "allowMergeCommit": allowMergeCommit,
                "allowRebaseMerge": allowRebaseMerge,
                "allowAutoMerge": allowAutoMerge,
                "deleteBranchOnMerge": deleteBranchOnMerge,
                "useSquashPrTitleAsDefault": useSquashPrTitleAsDefault,
                "squashMergeCommitTitle": squashMergeCommitTitle,
                "squashMergeCommitMessage": squashMergeCommitMessage,
                "mergeCommitTitle": mergeCommitTitle,
                "mergeCommitMessage": mergeCommitMessage,
                "customProperties": customProperties,
            }

            result = None

            async with session.post(
                url, headers=headers, data=json.dumps(data)
            ) as response:
                json_response = await response.json()
                bad_credentials = (
                    json_response.get("message", None) == "Bad credentials"
                )
                if response.status in [200, 201] and not bad_credentials:
                    result = Repository(
                        org,
                        name,
                        description,
                        homepage,
                        private,
                        visibility,
                        hasIssues,
                        hasWiki,
                        hasDownloads,
                        hasProjects,
                        teamId,
                        autoInit,
                        licenseTemplate,
                        gitignoreTemplate,
                        allowSquashMerge,
                        allowMergeCommit,
                        allowRebaseMerge,
                        allowAutoMerge,
                        deleteBranchOnMerge,
                        useSquashPrTitleAsDefault,
                        squashMergeCommitTitle,
                        squashMergeCommitMessage,
                        mergeCommitTitle,
                        mergeCommitMessage,
                        customProperties,
                    )

            return result

    async def rename_to(self, org: str, name: str, newName: str) -> bool:
        """
        Renames a Github repository.
        :param org: The name of the organization.
        :type org: str
        :param name: The name of the repository.
        :type name: str
        :param newNawe: The new name of the repository.
        :type newName: str
        :return: True if the operation was successful.
        :rtype: bool
        """
        async with aiohttp.ClientSession() as session:
            result = False
            headers = {
                "Authorization": f"token {self.token.get()}",
                "Content-Type": "application/json",
            }
            url = f"https://api.github.com/repos/{org}/{name}"

            data = {"name": newName}

            async with session.patch(url, headers=headers, json=data) as response:
                json_response = await response.json()
                bad_credentials = (
                    json_response.get("message", None) == "Bad credentials"
                )
                if response.status in [200, 201] and not bad_credentials:
                    result = True

            return result


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
