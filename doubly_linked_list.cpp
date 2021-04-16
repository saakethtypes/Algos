#include <iostream>;
using namespace std;

//print utils 
class printData {
   public:
      void print(int i) {
        cout << i << endl;
      }
      void print(double  f) {
        cout << f << endl;
      }
      void print(char* c) {
        cout << c << endl;
      }
};


//node struct
struct Node
{
    int data;
    struct Node* next = NULL;
    struct Node* prev = NULL;
};

//dll class
class DLL
{
  private:
    struct Node* head = NULL;
    struct Node* start = NULL;
    struct Node* end = NULL;
    int len;
  public:
    int insert(int x){
      struct Node* newNode = (struct Node*) malloc(sizeof(struct Node));
        if(head == NULL){
          newNode->data = x;
          head = newNode;
          start = head;
        }else{
          newNode->data = x;
          newNode->prev = head;
          head->next = newNode;
          head = newNode;
        }
      return 0;
  }

  int printList(){
    
    do{
      printData pd;
      pd.print(head->data);
      head = head->prev;
      len++;
    }while(head->prev != NULL);
    end = head;
    return 0;
  }
};

int main(void)
{
  DLL dll;
  dll.insert(2);
  dll.insert(4);
  dll.insert(6);
  dll.insert(8);
  dll.insert(10);
  dll.printList();
}

