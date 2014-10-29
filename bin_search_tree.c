#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct tree{
    int item;
    struct tree * parent;
    struct tree * left;
    struct tree * right;
} tree;

tree *search_tree(tree *l, int x)
{
    if(l==NULL) return(NULL);

    if(l->item == x ) return(l);
    
    if(x < l->item) 
        return( search_tree(l->left, x) );
    else {
        return( search_tree(l->right, x) );
    }
}

tree *find_minimum(tree *t)
{
    tree *min;

    if(t == NULL) return(NULL);

    min = t;
    while (min->left != NULL)
        min = min ->left;
    return(min);

}

void traverse_tree(tree *l)
{
    if(l != NULL) {
        traverse_tree(l->left);
        printf("tree item:  %i\n", l->item);
        traverse_tree(l->right);
    }
}

void insert_tree(tree **l, int x, tree *parent)
{
    tree *p;

    if (*l == NULL){
        p = malloc(sizeof(tree));
        p->item = x;
        p->left = p->right = NULL;
        p->parent = parent;
        *l = p;
        return;
    }

    if (x < (*l)->item)
        insert_tree(&((*l)->left), x, *l);
    else
        insert_tree(&((*l)->right), x, *l);
}

int main(){
   struct tree rt0, rt_l, rt_r, ll, lr, rl, rr;
   tree * rt_ptr = &rt0;  //pointer to the base root of the tree
   ll.item = 1;
   rt_l.item = 2;
   lr.item = 3;
   rt0.item = 4;
   rl.item = 5;
   rt_r.item = 6;
   rr.item = 7;

   ll.left = NULL;
   rt_l.left = &ll;
   lr.left = NULL;
   rt0.left = &rt_l;
   rl.left = NULL;
   rt_r.left = &rl;
   rr.left = NULL;
   
   ll.right = NULL;
   rt_l.right = &lr;
   lr.right = NULL;
   rt0.right = &rt_r;
   rl.right = NULL;
   rt_r.right = &rr;
   rr.right = NULL;

   //Tree function tests
   //int min = find_minimum(&rt0)->item;
   //printf("\nminimum:  %i\n", min);
   traverse_tree(&rt0);
   //insert_tree(&(rt0.left), 10,  &rt0);
   insert_tree(&rt_ptr, 999,  NULL);
   printf("\n");
   traverse_tree(&rt0);


   /*
   printf("&a:  %p,  a.item:  %s\n", &a,  (&a)->item);
   printf("&b:  %p,  b.item:  %s\n", a.next, a.next->item);
   printf("&c:  %p,  c.item:  %s\n", b.next, b.next->item);
   printf("c.next?  %p\n\n", c.next);

   //list *x = search_list(&a, "dog");
   printf("search result:  %p\n", search_list(&a, "cat"));*/

};
