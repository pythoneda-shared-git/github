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
from pythoneda.shared import attribute, BaseObject, primary_key_attribute
from pythoneda.shared.git import GitRepo
from typing import Dict, Union


class Repository(GitRepo):
    """
    Represents Github repositories.

    Class name: Repository

    Responsibilities:
        - Provides Github-specific Git repository logic.

    Collaborators:
        - None
    """

    def __init__(
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
    ):
        """
        Creates a new Repository instance.
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
        """
        super().__init__(f"https://github.com/{org}/{name}")
        self._org = org
        self._name = name
        self._description = description
        self._homepage = homepage
        self._private = private
        self._visibility = visibility
        self._has_issues = hasIssues
        self._has_projects = hasProjects
        self._has_wiki = hasWiki
        self._has_downloads = hasDownloads
        self._team_id = teamId
        self._auto_init = autoInit
        self._license_template = licenseTemplate
        self._gitignore_template = gitignoreTemplate
        self._allow_squash_merge = allowSquashMerge
        self._allow_merge_commit = allowMergeCommit
        self._allow_rebase_merge = allowRebaseMerge
        self._allow_auto_merge = allowAutoMerge
        self._delete_branch_on_merge = deleteBranchOnMerge
        self._use_squash_pr_title_as_default = useSquashPrTitleAsDefault
        self._squash_merge_commit_title = squashMergeCommitTitle
        self._squash_merge_commit_message = squashMergeCommitMessage
        self._merge_commit_title = mergeCommitTitle
        self._merge_commit_message = mergeCommitMessage
        self._custom_properties = customProperties

    @property
    @primary_key_attribute
    def org(self) -> str:
        """
        Retrieves the organization name.
        :return: Such name.
        :rtype: str
        """
        return self._org

    @property
    @primary_key_attribute
    def name(self) -> str:
        """
        Retrieves the repository name.
        :return: Such name.
        :rtype: str
        """
        return self._name

    @property
    @attribute
    def description(self) -> str:
        """
        Retrieves the repository description.
        :return: Such description.
        :rtype: str
        """
        return self._description

    @property
    @attribute
    def homepage(self) -> str:
        """
        Retrieves the repository homepage.
        :return: Such homepage.
        :rtype: str
        """
        return self._homepage

    @property
    @attribute
    def private(self) -> bool:
        """
        Retrieves the repository privacy.
        :return: True if private.
        :rtype: bool
        """
        return self._private

    @property
    @attribute
    def visibility(self) -> str:
        """
        Retrieves the repository visibility.
        :return: Such visibility.
        :rtype: str
        """
        return self._visibility

    @property
    @attribute
    def has_issues(self) -> bool:
        """
        Retrieves whether the repository has issues.
        :return: True if issues are enabled.
        :rtype: bool
        """
        return self._has_issues

    @property
    @attribute
    def has_projects(self) -> bool:
        """
        Retrieves whether the repository has projects.
        :return: True if projects are enabled.
        :rtype: bool
        """
        return self._has_projects

    @property
    @attribute
    def has_wiki(self) -> bool:
        """
        Retrieves whether the repository has a wiki.
        :return: True if the wiki is enabled.
        :rtype: bool
        """
        return self._has_wiki

    @property
    @attribute
    def has_downloads(self) -> bool:
        """
        Retrieves whether the repository has downloads.
        :return: True if downloads are enabled.
        :rtype: bool
        """
        return self._has_downloads

    @property
    @attribute
    def team_id(self) -> Union[int, None]:
        """
        Retrieves the team id.
        :return: Such id.
        :rtype: Union[int, None]
        """
        return self._team_id

    @property
    @attribute
    def auto_init(self) -> Union[bool, None]:
        """
        Retrieves whether the repository is auto-initialized.
        :return: True if auto-initialized.
        :rtype: Union[bool, None]
        """
        return self._auto_init

    @property
    @attribute
    def license_template(self) -> Union[str, None]:
        """
        Retrieves the license template.
        :return: Such template.
        :rtype: Union[str, None]
        """
        return self._license_template

    @property
    @attribute
    def gitignore_template(self) -> Union[str, None]:
        """
        Retrieves the gitignore template.
        :return: Such template.
        :rtype: Union[str, None]
        """
        return self._gitignore_template

    @property
    @attribute
    def allow_squash_merge(self) -> Union[bool, None]:
        """
        Retrieves whether squash-merging is allowed.
        :return: True if allowed.
        :rtype: Union[bool, None]
        """
        return self._allow_squash_merge

    @property
    @attribute
    def allow_merge_commit(self) -> Union[bool, None]:
        """
        Retrieves whether merge commits are allowed.
        :return: True if allowed.
        :rtype: Union[bool, None]
        """
        return self._allow_merge_commit

    @property
    @attribute
    def allow_rebase_merge(self) -> Union[bool, None]:
        """
        Retrieves whether rebase-merging is allowed.
        :return: True if allowed.
        :rtype: Union[bool, None]
        """
        return self._allow_rebase_merge

    @property
    @attribute
    def allow_auto_merge(self) -> Union[bool, None]:
        """
        Retrieves whether auto-merging is allowed.
        :return: True if allowed.
        :rtype: Union[bool, None]
        """
        return self._allow_auto_merge

    @property
    @attribute
    def delete_branch_on_merge(self) -> Union[bool, None]:
        """
        Retrieves whether branches are deleted on merge.
        :return: True if deleted.
        :rtype: Union[bool, None]
        """
        return self._delete_branch_on_merge

    @property
    @attribute
    def use_squash_pr_title_as_default(self) -> Union[bool, None]:
        """
        Retrieves whether the squash PR title is used as default.
        :return: True if used.
        :rtype: Union[bool, None]
        """
        return self._use_squash_pr_title_as_default

    @property
    @attribute
    def squash_merge_commit_title(self) -> Union[str, None]:
        """
        Retrieves the squash merge commit title.
        :return: Such title.
        :rtype: Union[str, None]
        """
        return self._squash_merge_commit_title

    @property
    @attribute
    def squash_merge_commit_message(self) -> Union[str, None]:
        """
        Retrieves the squash merge commit message.
        :return: Such message.
        :rtype: Union[str, None]
        """
        return self._squash_merge_commit_message

    @property
    @attribute
    def merge_commit_title(self) -> Union[str, None]:
        """
        Retrieves the merge commit title.
        :return: Such title.
        :rtype: Union[str, None]
        """
        return self._merge_commit_title

    @property
    @attribute
    def merge_commit_message(self) -> Union[str, None]:
        """
        Retrieves the merge commit message.
        :return: Such message.
        :rtype: Union[str, None]
        """
        return self._merge_commit_message

    @property
    @attribute
    def custom_properties(self) -> Union[Dict[str, str], None]:
        """
        Retrieves the custom properties.
        :return: Such properties.
        :rtype: Union[Dict[str, str], None]
        """
        return self._custom_properties

    async def renamed_to(self, newName: str) -> bool:
        """
        Checks if this repository has been renamed.
        :param newName: The new name.
        :type newName: str
        :return: True if renamed.
        :rtype: bool
        """
        return True

    async def rename_to(self, newName: str) -> None:
        """
        Renames this repository.
        :param newName: The new name.
        :type newName: str
        """
        pass


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
