"""
This module contains the Blog class.
"""
import requests


class Blog:
    """
    Blog class to represent a blog and its posts.
    """

    def __init__(self, name):
        """
        Initialize a blog with a name.
        
        :param name: The name of the blog.
        :type name: str
        """
        self.name = name

    def posts(self):
        """
        Get all posts for this blog.
        
        Using the requests library, a GET request is sent to the
        json placeholder API to retrieve all posts for this blog.
        
        :return: A list of JSON objects representing the posts.
        :rtype: list
        """
        response = requests.get("https://jsonplaceholder.typicode.com/posts")

        # Return the list of posts
        return response.json()

    def __repr__(self):
        """
        Return a string representation of the Blog object.
        """
        return f'<Blog: {self.name}>'
