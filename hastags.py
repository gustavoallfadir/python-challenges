'''
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

    It must start with a hashtag (#).
    All words must have their first letter capitalized.
    If the final result is longer than 140 chars it must return false.
    If the input or the result is an empty string it must return false.
'''

def generate_hashtag(s):
    return ''.join(['#' , ''.join([w.title() for w in s.split(' ')])]) if len(s) > 0 and len(s) < 140 else False


print(generate_hashtag('because we love coffee'))
print(generate_hashtag('hakuna matata'))
print(generate_hashtag(''))
print(generate_hashtag('this is a long string supposed to return false because it exceeds the limit of 140 characters so at this point the creator is just typing random stuff to fill'))