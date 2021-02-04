def post_traversal(self):
    if(self.left):
        self.left.post_traversal()
    if(self.right):
        self.right.post_traversal()
    
    print(self.value)