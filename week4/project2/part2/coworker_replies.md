# Replies from V. Vaughn

V. Vaughn left the team in March. These are real replies to real questions,
pulled from the old chat logs and pasted here in no particular order.

**Do not open this file until at least four entries are written in
question_log.md.** The point of Part 2 is the process of getting stuck, and
reading ahead throws that away. The replies are reproduced exactly as they
were sent, which means some of them are more useful than others.

---

**Q: what does ranking() actually give back?**

> a list of pet indices, best first. so if it comes back `[2, 1, 0]` that
> adopter wants pet 2 most and pet 0 least. it's a copy, you can mess with it

---

**Q: load() is throwing a ValueError on the preferences file, is the file bad?**

> hm, works on my machine. I've always fed it the file straight out of the
> export script and never had a problem. try regenerating it?

---

**Q: is rank_of 1-based or 0-based?**

> zero based, same as everything else in there. the README example is right

---

**Q: README says popularity_order goes least popular to most popular, is that still true?**

> I'd trust the README on that one. I did fiddle with the sort key at some
> point but I'm fairly sure the direction is the same as it always was

---

**Q: do any of the check functions modify the matching I pass in?**

> they're all pretty cheap, none of them copy the matching so you don't have
> to worry about memory even on the big inputs

---

**Q: what happens if I call ranking() with an adopter id that isn't in the table?**

> check the README, I'm pretty sure that's covered

---

**Q: table.rows doesn't exist, has it been renamed?**

> ah yeah that's ancient, ignore that bit of the README. just use the methods,
> they're fine

---

**Q: what does best_match return?**

> it tells you whether it's the best match. it's been in there since the
> prototype, name's a bit off but it does what you'd want
