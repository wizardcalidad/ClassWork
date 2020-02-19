"""The NPR radio show Car Talk always offers a puzzle to solve. Occasionally, one can be
solved with a program. Try this one: My car’s odometer measures distance traveled in
whole numbers—no tenths of miles—up to 999,999. Last week I was driving along on
the freeway and noticed that the last four digits, but not the last five digits, formed a
palindrome; that is, it read the same backward as forward (e.g., 1221). After one mile
went by, though, the last five digits did form a palindrome; and, after one more mile,
the middle four digits formed a palindrome. Finally, when the third mile rolled over,
all six digits formed a palindrome. What was my mileage at the time I first noticed all
these palindromes?"""

for mile in range(10_000, 1_000_000):
    mile_str = str(mile)

    last_four = mile_str[-4:]
    last_five = mile_str[-5:]

    if (last_four == last_four[::-1]) and (last_five != last_five[::-1]):
        mile_str = str(mile + 1)
        last_five = mile_str[-5:]

        if(last_five==last_five[::-1]):
            mile_str = str(mile + 2)
            mid_four = mile_str[1:5]

            if(mid_four == mid_four[::-1]):
                mile_str = str(mile + 3)

                if(mile_str == mile_str[::-1]):
                    print(f"the mile is = {mile}")




