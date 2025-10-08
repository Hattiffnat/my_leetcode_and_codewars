fn solution(word: &str, ending: &str) -> bool {
    let mut word_iter = word.chars().rev();

    for end_ch in ending.chars().rev() {
        match word_iter.next() {
            Some(word_ch) => {
                if word_ch != end_ch {
                    return false;
                }
            }
            None => { return false }
        }
    }
    true
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn returns_expected() {
        assert_eq!(true, solution("abc", "c"));
        assert_eq!(false, solution("strawberry", "banana"));
    }
}
