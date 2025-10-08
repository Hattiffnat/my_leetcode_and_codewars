use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut last_index: HashMap<char, usize> = HashMap::new();

        let mut max = 0;
        let mut count = 0;

        let mut substr_first: usize = 0;

        for (i, ch) in s.chars().enumerate() {
            match last_index.get(&ch) {
                Some(index) => {
                    if count > max { max = count }

                    match index.checked_sub(substr_first) {
                        Some(diff) => {
                            count -= diff;
                            substr_first = index + 1
                        }
                        None => {
                            count += 1
                        }
                    }

                    last_index.insert(ch, i);
                },
                None => {
                    last_index.insert(ch, i);
                    count += 1;
                }
            }
        }

        if count > max { max = count }

        max as i32
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn sub_test() {
        dbg!(3usize.checked_sub(1usize));
    }

    #[test]
    fn it_works() {
        assert!(
            Solution::length_of_longest_substring("abcabcbb".to_string()) == 3,
            "abcabcbb"
        );
        assert!(
            Solution::length_of_longest_substring("bbbbb".to_string()) == 1,
            "bbbbb"
        );
        assert!(
            dbg!(Solution::length_of_longest_substring("pwwkew".to_string())) == 3,
            "pwwkew"
        );
        assert!(
            dbg!(Solution::length_of_longest_substring("dvdf".to_string())) == 3,
            "dvdf"
        );
        assert!(
            dbg!(Solution::length_of_longest_substring("abba".to_string())) == 2,
            "abba"
        );
        assert!(
            dbg!(Solution::length_of_longest_substring("tmmzuxt".to_string())) == 5,
            "tmmzuxt"
        );
    }
}
