struct Solution;

use std::collections::VecDeque;

impl Solution {
    pub fn snakes_and_ladders(board: Vec<Vec<i32>>) -> i32 {
        let n = board.len();
        let mut flatboard = Vec::<i32>::new();

        let mut toggle = true;
        for row in board.iter().rev() {
            if toggle {
                flatboard.extend(row.iter());
            } else {
                flatboard.extend(row.iter().rev());
            }
            toggle = !toggle;
        }

        let (mut q, mut best) = (VecDeque::new(), vec![-1; (n * n) as usize]);
        q.push_back(0);
        best[0] = 0;

        while let Some(index) = q.pop_front() {
            for i in index + 1..(index + 7).min(n * n) {
                let mut new_index = i;

                if flatboard[new_index] != -1 {
                    new_index = (flatboard[new_index] - 1) as usize;
                }

                if new_index == (n * n) - 1 {
                    return best[index] + 1;
                }

                if best[new_index] == -1 {
                    q.push_back(new_index);
                    best[new_index] = best[index] + 1;
                }
            }
        }

        -1
    }
}

fn slices_to_vec(slices: &[&[i32]]) -> Vec<Vec<i32>> {
    let mut res: Vec<Vec<i32>> = Vec::new();

    for slice in slices {
        res.push(slice.to_vec())
    }

    res
}

fn main() {
    // let board = slices_to_vec(&[&[-1, -1], &[-1, 3]]);
    // assert_eq!(Solution::snakes_and_ladders(board), 1);

    // let board = slices_to_vec(&[&[-1, -1, -1], &[-1, 9, 8], &[-1, 8, 9]]);
    // assert_eq!(Solution::snakes_and_ladders(board), 1);

    // let board = slices_to_vec(&[&[-1, 7, -1], &[-1, 6, 9], &[-1, -1, 2]]);
    // assert_eq!(Solution::snakes_and_ladders(board), 1);

    // let board = slices_to_vec(&[
    //     &[-1, -1, 19, 10, -1],
    //     &[2, -1, -1, 6, -1],
    //     &[-1, 17, -1, 19, -1],
    //     &[25, -1, 20, -1, -1],
    //     &[-1, -1, -1, -1, 15],
    // ]);
    // assert_eq!(Solution::snakes_and_ladders(board), 2);

    let board = slices_to_vec(&[
        &[-1, 10, -1, 15, -1],
        &[-1, -1, 18, 2, 20],
        &[-1, -1, 12, -1, -1],
        &[2, 4, 11, 18, 8],
        &[-1, -1, -1, -1, -1],
    ]);
    assert_eq!(Solution::snakes_and_ladders(board), 3);
}
