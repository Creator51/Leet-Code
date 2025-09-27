/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head == nullptr || head->next == nullptr)
            return false;
        
        ListNode * temp = head;
        ListNode * fast=temp->next;
        ListNode * slow=temp;
        while(fast!=nullptr && fast->next!=nullptr){
            
            if(slow==fast){
            return true;
            break;
            }
            slow=slow->next;
            fast=fast->next->next;

        }
        return false;

        
    }
};