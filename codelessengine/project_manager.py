from .config import ConfigParser


class ProjectManager:

    def __init__(self):
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)


class Project:

    def __init__(self, config_file):
        self.config = ConfigParser(config_file)
