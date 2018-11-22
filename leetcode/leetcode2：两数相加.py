class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummyHead = ListNode(0)
        p = l1
        q = l2
        curr = dummyHead
        carry = 0
        while p!=None or q!= None:
            if p == None:
                x = 0
            else:
                x = p.val 
                
            if q == None:
                y = 0
            else:
                y = q.val
                
            sum = x+y+carry
            curr.next=ListNode(sum%10) 
            curr = curr.next
            carry = sum/10
            
            if p != None:
                p = p.next
            if q != None:
                q = q.next
        
        if carry != 0:
            curr.next = ListNode(carry)
         
        return dummyHead.next