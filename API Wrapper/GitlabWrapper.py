#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
from requests.auth import HTTPBasicAuth
from GitlabToken import token

####################################################################
# Gitlab API Wrapper
####################################################################

class GitlabWrapper:
    
    # GET gitlab/groups/:id/members
    @staticmethod
    def get_group_members(group_id):
        """
        get all public & private members of the group.
        outputs member html url, member username, member name
        Return type: dict 
        """
        base_url = "https://gitlab.com/api/v4/"
        base_url = base_url+"groups/{}/members".format(group_id)
        result = requests.get(base_url, headers={"Private-Token":token }).text
        members = json.loads(result)
        members_dict = {}
        i = 1
        for member in members:
            member_dict = {}
            member_dict['username'] = member['username']
            member_dict['name'] = member['name']
            member_dict['url'] = member['web_url']
            members_dict[i] = member_dict
            i += 1
        return members_dict

    # GET gitlab/groups/:id/projects
    @staticmethod
    def get_group_projects(group_id):
        """
        get projectsitories of the group.
        outputs project html url, project full name
        Return type: dict 
        """

        base_url = "https://gitlab.com/api/v4/"
        base_url = base_url+"groups/{}/projects".format(group_id)
        result = requests.get(base_url, headers={"Private-Token":token }).text
        projects = json.loads(result)
        projects_dict = {}
        i = 1
        for project in projects:
            project_dict = {}
            project_dict['name'] = project['name']
            project_dict['url'] = project['web_url']
            project_dict['id'] = project['id']
            projects_dict[i] = project_dict
            i += 1
        return projects_dict

    # GET gitlab/projects/:id/repository/commits
    @staticmethod
    def get_project_commits(project_id):
        """
        get project commits.
        outputs commit author, commit url, commit sha
        Return type: dict 
        """
        base_url = "https://gitlab.com/api/v4/"
        base_url = base_url+"projects/{}/repository/commits".format(project_id)
        result = requests.get(base_url, headers={"Private-Token":token }).text
        commits = json.loads(result)
        commits_dict = {}
        i = 1
        for commit in commits:
            commit_dict = {}
            commit_dict['author'] = commit['author_name']
            commit_dict['message'] = commit['message'] 
            commit_dict['id'] = commit['id']
            commits_dict[i] = commit_dict
            i += 1
        return commits_dict

    # GET gitlab/projects/:id/issues
    @staticmethod
    def get_project_issues(project_id):
        """
        get project issues only.
        outputs issue tile, issue url, id
        Return type: dict 
        """
        base_url = "https://gitlab.com/api/v4/"
        base_url = base_url+"projects/{}/issues".format(project_id)
        result = requests.get(base_url, headers={"Private-Token":token }).text
        issues = json.loads(result)

        issues_dict = {}
        i = 1
        for issue in issues:
            issue_dict = {}
            issue_dict['id'] = issue["id"]
            issue_dict['iid'] = issue["iid"]
            issue_dict['title'] = issue["title"]
            issue_dict['url'] = issue["web_url"]
            issue_dict['description'] = issue["description"]
            issue_dict['labels'] = []
            for label in issue["labels"]:
                issue_dict['labels'].append(label)
            issues_dict[i] = issue_dict
            i += 1
        return issues_dict

    # GET gitlab/groups/:id/issues
    @staticmethod
    def get_group_issues(group_id):
        """
        get all groups issues, project wise
        outputs projectname: issue title, issue url
        Return type: dict 
        """
        base_url = "https://gitlab.com/api/v4/"
        base_url = base_url+"groups/{}/issues".format(group_id)
        result = requests.get(base_url, headers={"Private-Token":token }).text
        issues = json.loads(result)
        issues_dict = {}
        i = 1
        for issue in issues:
            issue_dict = {}
            issue_dict['id'] = issue["id"]
            issue_dict['iid'] = issue["iid"]
            issue_dict['title'] = issue["title"]
            issue_dict['url'] = issue["web_url"]
            issue_dict['description'] = issue["description"]
            issue_dict['labels'] = []
            for label in issue["labels"]:
                issue_dict['labels'].append(label)
            issues_dict[i] = issue_dict
            i += 1
        return issues_dict

    # GET gitlab/projects/:id/issues/:issue_iid/notes
    @staticmethod
    def get_issue_comments_dict(project_id, issue_iid):
        """
        get project issues only.
        outputs issue tile, issue url, id
        Return type: dict 
        """
        base_url = "https://gitlab.com/api/v4/"
        base_url_issues_comments = base_url+"projects/{}/issues/{}/notes"
        comments_result = requests.get(base_url_issues_comments.format(project_id, issue_iid), headers={"Private-Token":token }).text
        comments = json.loads(comments_result)
        comments_dict = {}
        i = 1
        for comment in comments:
            comment_dict = {}
            comment_dict['body'] = comment['body']
            comments_dict[i] = comment_dict
            i += 1
        return comments_dict
    

    # GET gitlab/projects/:id/merge_requests
    @staticmethod
    def get_project_merge_request(project_id):
        """
        get all project pull requests
        outputs index: pull name, pull url
        Return type: dict 
        """
        base_url = "https://gitlab.com/api/v4/"
        base_url = base_url+"projects/{}/merge_requests".format(project_id)
        result = requests.get(base_url, headers={"Private-Token":token }).text
        merge_requests = json.loads(result)

        merge_requests_dict = {}
        i = 1
        for merge_request in merge_requests:
            merge_request_dict = {}
            merge_request_dict['id'] = merge_request["id"]
            merge_request_dict['title'] = merge_request["title"]
            merge_request_dict['url'] = merge_request["web_url"]
            merge_request_dict['description'] = merge_request["description"]
            merge_requests_dict[i] = merge_request_dict
            i += 1
        return merge_requests_dict