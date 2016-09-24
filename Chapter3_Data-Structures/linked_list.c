#include <stdio.h>
#include <string.h>

typedef struct list{
    char item[50];
    struct list *next;
} list;

list *search_list(list *l, char x[])
{
    if(l==NULL) return(NULL);

    if(strcmp(l->item,  x)==0){
        return(l);
    }
    else {
        return(search_list(l->next, x));
    }
}

int main(){
   struct list a, b, c;
   strcpy(a.item, "dog");
   strcpy(b.item, "cat");
   strcpy(c.item, "hare");
   a.next = &b;
   b.next = &c;
   c.next = NULL;
   

   printf("&a:  %p,  a.item:  %s\n", &a,  (&a)->item);
   printf("&b:  %p,  b.item:  %s\n", a.next, a.next->item);
   printf("&c:  %p,  c.item:  %s\n", b.next, b.next->item);
   printf("c.next?  %p\n\n", c.next);

   //list *x = search_list(&a, "dog");
   printf("search result:  %p\n", search_list(&a, "cat"));

};
