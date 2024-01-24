# vim: set fileencoding=utf-8
"""
pythoneda/shared/git/github/repository.py

This file defines the Repository class.

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
from github import Auth, Github
from pythoneda.shared import BaseObject
from typing import Dict, Union


class Repository(BaseObject):
    """
    Interacts with the /orgs/[org]/repos endpoint of github API.

    Class name: Repository

    Responsibilities:
        - Know how to use the github API to manage repositories.

    Collaborators:
        - None
    """

    def __init__(self, token: str):
        """
        Creates a new Repository instance.
        """
        super().__init__()
        self._token = token
        self._github = Github(auth=Auth.Token(token))

    @property
    def token(self) -> str:
        """
        Retrieves the github token.
        :return: Such token.
        :rtype: str
        """
        return self._token

    @property
    def github(self) -> Github:
        """
        Retrieves the github.Github instance.
        :return: Such instance.
        :rtype: github.Github
        """
        return self._github

    def create(
        self,
        name: str,
        description: Union[str, github.GithubObject._NotSetType] = NotSet,
        homepage: Union[str, github.GithubObject._NotSetType] = NotSet,
        private: Union[bool, github.GithubObject._NotSetType] = NotSet,
        visibility: Union[str, github.GithubObject._NotSetType] = NotSet,
        hasIssues: Union[bool, github.GithubObject._NotSetType] = NotSet,
        hasWiki: Union[bool, github.GithubObject._NotSetType] = NotSet,
        hasDownloads: Union[bool, github.GithubObject._NotSetType] = NotSet,
        hasProjects: Union[bool, github.GithubObject._NotSetType] = NotSet,
        teamId: Union[int, github.GithubObject._NotSetType] = NotSet,
        autoInit: Union[bool, github.GithubObject._NotSetType] = NotSet,
        licenseTemplate: Union[str, github.GithubObject._NotSetType] = NotSet,
        gitignoreTemplate: Union[str, github.GithubObject._NotSetType] = NotSet,
        allowSquashMmerge: Union[bool, github.GithubObject._NotSetType] = NotSet,
        allowMergeCommit: Union[bool, github.GithubObject._NotSetType] = NotSet,
        allowRebaseMerge: Union[bool, github.GithubObject._NotSetType] = NotSet,
        allowAutoMerge: Union[bool, github.GithubObject._NotSetType] = NotSet,
        deleteBranchOnMerge: Union[bool, github.GithubObject._NotSetType] = NotSet,
        useSquashPrTitleAsDefault: Union[
            bool, github.GithubObject._NotSetType
        ] = NotSet,
        squashMergeCommitTitle: Union[str, github.GithubObject._NotSetType] = NotSet,
        squashMergeCommitMessage: Union[str, github.GithubObject._NotSetType] = NotSet,
        mergeCommitTitle: Union[str, github.GithubObject._NotSetType] = NotSet,
        mergeCommitMessage: Union[str, github.GithubObject._NotSetType] = NotSet,
        customProperties: Union[
            Dict[str, str], github.GithubObject._NotSetType
        ] = NotSet,
    ) -> github.Repository.Repository:
        """
        Creates a new repository.
        :param name: The repository name.
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
        """
        return self.github.create_repo(
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
            allowSquashMmerge,
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


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
