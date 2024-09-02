struct Solution;

impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        let gen_len = nums1.len() + nums2.len();

        let mut k = 0;
        let mut j = 0;

        let mut both = Vec::new();
        for _i in 0..(gen_len / 2 + 1) {

            if k < nums1.len() && nums1[k] < nums2[j] {
                both.push(nums1[k]);
                k += 1;
            } else if j < nums2.len() {
                both.push(nums2[j]);
                j += 1;
            }
        };

        if (gen_len % 2) == 0 {
            return (both.pop().unwrap() + both.pop().unwrap()) as f64 / 2.0;
        } else {
            return both.pop().unwrap() as f64;
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        assert_eq!(dbg!(Solution::find_median_sorted_arrays(vec![1, 3], vec![2])), 2.0);
        assert_eq!(dbg!(Solution::find_median_sorted_arrays(vec![1,2], vec![3,4])), 2.5);
        assert_eq!(dbg!(Solution::find_median_sorted_arrays(vec![], vec![3,4])), 3.5);
        assert_eq!(dbg!(Solution::find_median_sorted_arrays(vec![0, 0], vec![0, 0])), 0.0);
    }
}
