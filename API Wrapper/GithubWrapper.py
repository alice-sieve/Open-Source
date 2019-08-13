#!/usr/bin/python
# -*- coding: utf-8 -*-
from github import Github
from datetime import datetime, timezone
from GithubToken import github_token, user, password


####################################################################
# Github API Wrapper
####################################################################

class GithubWrapper:

    def __init__(self):
        """
        handles user authentication &
        creates user object
        """

        if github_token is None:
            self.user_obj = Github(user, password)
        else:
            self.user_obj = Github(github_token)

    def get_org_obj(self, organization):
        """
        creates oraganization object
        Return type: <class 'github.Organization.Organization'>
        """

        self.org_obj = self.user_obj.get_organization(organization)
        return self.org_obj

    
    def get_user_name(self, username):
        """
         find name for given username 
         Return type: string
         """

        user = self.user_obj.get_user(username)
        return user.name

    
    def get_org_members(self, organization):
        """
        get all public & private members of the org.
        outputs member html url, member username, member name
        Return type: dict 
        """

        org_obj = self.get_org_obj(organization)
        members_dict = {}
        members = org_obj.get_members()
        i = 1
        for member in members:
            member_dict = {}
            member_dict['username'] = member._identity
            member_dict['name'] = \
                self.user_obj.get_user(member._identity).name
            member_dict['url'] = member.html_url
            members_dict[i] = member_dict
            i += 1
        return members_dict

    
    def get_org_repos(self, organization):
        """
        get repositories of the org.
        outputs repo html url, repo full name
        Return type: dict 
        """

        org_obj = self.get_org_obj(organization)
        repos = org_obj.get_repos()
        repos_dict = {}
        i = 1
        for repo in repos:
            repo_dict = {}
            repo_dict['full_name'] = repo.full_name
            repo_dict['url'] = repo.url
            repos_dict[i] = repo_dict
            i += 1
        return repos_dict

    
    def get_repo_commits(self, repository):
        """
        get repo commits.
        outputs commit author, commit url, commit sha
        Return type: dict 
        """

        repo = self.user_obj.get_repo(repository)
        commits = repo.get_commits()
        commits_dict = {}
        i = 1
        for commit in commits:
            commit_dict = {}
            commit_dict['author'] = commit.author.login
            commit_dict['url'] = commit.html_url
            commit_dict['sha'] = commit.sha
            commits_dict[i] = commit_dict
            i += 1
        return commits_dict

    
    def get_repo_issues(self, repository):
        """
        get repository issues only.
        outputs issue tile, issue url, id
        Return type: dict 
        """

        repo = self.user_obj.get_repo(repository)
        issues = repo.get_issues()
        issues_dict = {}
        i = 1
        for issue in issues:
            issue_dict = {}
            issue_dict['id'] = issue.id
            issue_dict['title'] = issue.title
            issue_dict['url'] = issue.url
            issue_dict['labels'] = []
            for label in issue.labels:
                issue_dict['labels'].append(label.name)
            issues_dict[i] = issue_dict
            i += 1
        return issues_dict

    
    def get_org_issues(self, organization):
        """
        get all orgs issues, repo wise
        outputs reponame: issue title, issue url
        Return type: dict 
        """

        org_obj = self.user_obj.get_organization(organization)
        repos = org_obj.get_repos()
        org_issues_dict = {}
        for repo in repos:
            issues_dict = self.get_repo_issues(repo.full_name)
            org_issues_dict[repo.full_name] = issues_dict
        return org_issues_dict

    
    def get_issue_comments_dict(self, repository):
        """
        get issue comments
        outputs index: issue title, issue url, comments
        Return type: dict 
        """

        repo = self.user_obj.get_repo(repository)
        issues = repo.get_issues()
        issues_dict = {}
        i = 1
        for issue in issues:
            issue_dict = {}
            issue_dict['url'] = issue.url
            issue_dict['title'] = issue.title
            issue_dict['comments'] = [comment.body for comment in issue.get_comments()]
            issues_dict[i] = issue_dict
            i += 1
        return issues_dict
    
    
    def get_repo_pulls(self, repository):
        """
        get all repo pull requests
        outputs index: pull name, pull url
        Return type: dict 
        """

        repo = self.user_obj.get_repo(repository)
        pulls = repo.get_pulls()
        pulls_dict = {}
        i = 1
        for pull in pulls:
            pull_dict = {}
            pull_dict['url'] = pull.url
            pull_dict['title'] = pull.title
            pull_dict['merged'] = pull.is_merged()
            pulls_dict[i] = pull_dict
            i += 1
        return pulls_dict


    # Must have push access to view repository collaborators.
    # def get_repo_contributers(self, repository):
    #     """
    #     get repo contributers
    #     contributers username, name, url
    #     Return type: dict
    #     """
    #     repo = self.user_obj.get_repo(repository)
    #     collaborators = repo.get_collaborators()
    #     collaborators_dict = {}
    #     i = 1
    #     for collaborator in collaborators:
    #         collaborator_dict = {}
    #         collaborator_dict["collaborator_username"] = collaborator._identity
    #         collaborator_dict["collaborator_url"] = collaborator.html_url
    #         collaborator_dict["collaborator_name"] = self.user_obj.get_user(collaborator._identity).name
    #         collaborators_dict[i] = collaborator_dict
    #         i+=1
    #     return collaborators_dict