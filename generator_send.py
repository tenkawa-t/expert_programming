def psychologist():
    print('あなたの悩みを聞かせてください')
    while True:
        answer = (yield)
        if answer is not None:
            if answer.endswith('?'):
                print('自分自身に問いかけをしないようしましょう')
            elif '良い' in answer:
                print('それは良いですね。ぜひやりましょう')
            elif '悪い' in answer:
                print('悲観的にならないようにしましょう')

free = psychologist()
next(free)
free.send('気分が悪いです')
free.send('なぜ私はすべきではないんでしょうか?')
free.send('なるほど。それなら何か私にとって良いかを探すべきですね')