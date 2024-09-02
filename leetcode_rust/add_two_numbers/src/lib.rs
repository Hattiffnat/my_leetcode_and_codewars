// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }

    fn from_list(list: &[i32]) -> Self{
        let mut iter_list = list.into_iter();

        let mut res = Self {
            val: iter_list.next().unwrap().clone(),
            next: None
        };

        let mut node = &mut res;

        for i in iter_list {
            node.next = Some(Box::new(ListNode { val: *i, next: None }));

            node = node.next.as_mut().unwrap()
        }

        res
    }
}

fn listnode_to_number(x: &ListNode) -> usize {
    let mut res = x.val as usize;
    let mut base = 10;

    let mut node_op = &x.next;

    while node_op.is_some() {
        let node = node_op.as_ref().unwrap();

        res += base * node.val as usize;
        base *= 10;

        node_op = &node.next;
    }

    res
}

fn number_to_listnode(x: usize) -> ListNode {
    let mut num = x;
    let base = 10;

    let mut res = ListNode { val: (num % base) as i32, next: None };
    num /= base;

    let mut node = &mut res;

    while num != 0 {
        node.next = Some(Box::new(ListNode {
            val: (num % base) as i32,
            next: None,
        }));

        num /= base;

        node = node.next.as_mut().unwrap()
    }

    res
}

pub fn _add_two_numbers(
    l1: Option<Box<ListNode>>,
    l2: Option<Box<ListNode>>,
) -> Option<Box<ListNode>> {
    Some(Box::new(number_to_listnode(
        listnode_to_number(l1.unwrap().as_ref()) + listnode_to_number(l2.unwrap().as_ref()),
    )))
}

pub fn add_two_numbers(
    l1: Option<Box<ListNode>>,
    l2: Option<Box<ListNode>>,
) -> Option<Box<ListNode>> {
    let mut x = &l1;
    let mut y = &l2;

    let mut sum = 0;
    let (mut div, mut rem) = (0, 0);

    let mut res = ListNode::new(0);
    let mut node = &mut res;

    loop {
        sum = div;

        sum += match x.as_ref() {
            Some(next_node) => next_node.val,
            None => 0
        };
        sum += match y.as_ref() {
            Some(next_node) => next_node.val,
            None => 0
        };

        (div, rem) = (sum / 10, sum % 10);

        node.val = rem;

        x = match x.as_ref() {
            Some(node) => &node.next,
            None => &None
        };
        y = match y.as_ref() {
            Some(node) => &node.next,
            None => &None
        };

        if !(x.is_some() || y.is_some() || div > 0) { break }

        node.next = Some(Box::new(ListNode::new(0)));
        node = node.next.as_mut().unwrap();
    }

    Some(Box::new(res))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn length() {
        dbg!(u128::MAX.to_string().len());
    }

    #[test]
    fn from_list() {
        let x = dbg!(ListNode::from_list(&[1,9,9,9,9,9,9,9,9,9]));
        dbg!(listnode_to_number(&x));
    }

    #[test]
    fn convert() {
        assert_eq!(
            listnode_to_number(&number_to_listnode(235)), 235
        );
    }

    #[test]
    fn nodes_equality() {
        let l1 = ListNode::from_list(&[2, 4, 3]);
        let l2 = l1.clone();

        assert_eq!(l1, l2)
    }

    #[test]
    fn summ() {
        let l1 = ListNode::from_list(&[2, 4, 3]);
        let l2 = ListNode::from_list(&[5, 6, 4]);

        let res = ListNode::from_list(&[7, 0, 8]);

        assert_eq!(
            dbg!(add_two_numbers(Some(Box::new(l1)), Some(Box::new(l2)))),
            Some(Box::new(res))
        )
    }
}
