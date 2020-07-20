package main.java.com.untitled;

class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class LL {
    public static ListNode removeElements(ListNode head, int val) {
        if (head == null) {
            return head;
        }

        ListNode dummy = new ListNode(-1, head);
        ListNode prev = dummy;
        while (head != null) {
            if (head.val == val) {
                prev.next = head.next;
            } else {
                prev = prev.next;
            }
            head = head.next;
        }
        return dummy.next;
    }

    public static void main(String[] args) {
        ListNode listNode1 = new ListNode(1);
        ListNode listNode2 = new ListNode(1);
        ListNode listNode3 = new ListNode(1);
        listNode1.next = listNode2;
        listNode2.next = listNode3;
        ListNode listNode = removeElements(listNode1, 1);
    }
}