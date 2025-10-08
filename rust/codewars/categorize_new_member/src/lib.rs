fn one_item(age: &i32, handicap: &i32) -> String {
    if *age < 55 || *handicap < 7 {
        return "Open".to_string();
    }

    "Senior".to_string()
}

fn open_or_senior(data: Vec<(i32, i32)>) -> Vec<String> {
    let mut res = Vec::new();

    for (age, handicap) in data {
        res.push(one_item(&age, &handicap))
    }

    res
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn returns_expected() {
        assert_eq!(
            open_or_senior(vec![(45, 12), (55, 21), (19, -2), (104, 20)]),
            vec!["Open", "Senior", "Open", "Senior"]
        );
        assert_eq!(
            open_or_senior(vec![(3, 12), (55, 1), (91, -2), (54, 23)]),
            vec!["Open", "Open", "Open", "Open"]
        );
    }
}
