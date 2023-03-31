#include <stdio.h>
#include <stdlib.h>

struct node {
  int item;
  struct node* left;
  struct node* right;
};

// Inorder traversal
void inorderTraversal(struct node* root) {
  if (root == NULL) return;
  inorderTraversal(root->left);
  printf("%d ->", root->item);
  inorderTraversal(root->right);
}

// Preorder traversal
void preorderTraversal(struct node* root) {
  if (root == NULL) return;
  printf("%d ->", root->item);
  preorderTraversal(root->left);
  preorderTraversal(root->right);
}

// Postorder traversal
void postorderTraversal(struct node* root) {
  if (root == NULL) return;
  postorderTraversal(root->left);
  postorderTraversal(root->right);
  printf("%d ->", root->item);
}

// Create a new Node
struct node* createNode(value) {
  struct node* newNode = malloc(sizeof(struct node));
  newNode->item = value;
  newNode->left = NULL;
  newNode->right = NULL;

  return newNode;
}

// Insert on the left of the node
struct node* insertLeft(struct node* current, int value) {
  current->left = createNode(value);
  return current->left;
}

// Insert on the right of the node
struct node* insertRight(struct node* current, int value) {
  current->right = createNode(value);
  return current->right;
}

int main() {
  struct node* root = createNode(4);
  insertLeft(root, 3);            
  insertRight(root, 6);                   
  insertLeft(root->left, 2);
  insertLeft(root->left->left,1);
  insertRight(root->left,5);
  /*
            4
           / \
          3   6
        / |   
       2  5
       |
       1

  */      

  printf("Inorder traversal \n");
  inorderTraversal(root); //lewy->print->prawy
  //idze po lewej az od konca, wypisuje lewy, pozniej prawe rodzenstwo
  //rekurencyjnie dla lewej, pozniej dla prawej

  printf("\nPreorder traversal \n");
  preorderTraversal(root);//print->lewy->prawy
  //rekurencyjnie zawsze najpierw lewy pozniej prawy


  printf("\nPostorder traversal \n");//lewy->prawy->print
  postorderTraversal(root);

  printf("\nPreorder traveras not from root \n");
  preorderTraversal(root->left);

  
}