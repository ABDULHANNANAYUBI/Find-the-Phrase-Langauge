lang_dataset = {
    "lang1": "The gladdest moment in life is a departure into unknown lands. Travel makes one modest. You see what a tiny place you occupy in the world. Better to see something once than hear about it a thousand times.",
    "lang2": "İnsan hayatındaki en mutlu an, bilinmeyen topraklara doğru yola çıkmaktır. Seyahat bir mütevazı yapar. Dünyada ne kadar küçük bir yer işgal ett",
    "lang3": "Радісний момент у житті людини це опинитися на невідомих землях. Подорож робить тебе скромним. Ти бачиш, яке маленьке місце займаєш у світі. Краще побачити щось один раз, ніж почути про це тисячу разів."
}
phrase = "ThIs Is hAppy Life"

phrase = phrase.lower().split(' ')
dataset = []

for key in range(len(lang_dataset)):
   dataset.append(list(lang_dataset.values())[key].lower())

counter_list = []

def solution(phrase):
    counter = 0
    for i in range(0, len(dataset)):
        for key in phrase:
            if key in dataset[i]:
                counter = counter + 1
        counter_list.append(counter)
        counter = 0
    if max(counter_list) > 0:
        return list(lang_dataset.keys())[counter_list.index(max(counter_list))]
    else:
        return 'No language found...!'

print(solution(phrase));
