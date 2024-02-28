#!/usr/bin/python3

from models.engine.db_storage import DBStorage
from models.author import Author
from models.citation import Citation

# Initialize the DBStorage engine
db_storage = DBStorage()
db_storage.reload()

# Define authors and their citations
authors_info = [
    {
        "name": "Mark Twain",
        "citations": [
            "The secret of getting ahead is getting started.",
            "The best way to cheer yourself up is to try to cheer somebody else up.",
            "Keep away from people who try to belittle your ambitions.",
            "Always do what is right. It will gratify half of mankind and astound the other.",
        ],
    },
    {
        "name": "Harry S. Truman",
        "citations": [
            "Nearly every crisis seems to be the worst one, but after it's over, it isn't so bad.",
            "How many times do you have to get hit over the head until you figure out who's hitting you?",
            "It is amazing what you can accomplish if you do not care who gets the credit.",
        ],
    },
    {
        "name": "Albert Einstein",
        "citations": [
            "If you can't explain it simply, you don't understand it well enough.",
            "The important thing is not to stop questioning. Curiosity has its own reason for existing.",
            "He who can no longer pause to wonder and stand rapt in awe, is as good as dead; his eyes are closed.",
            "Life is like riding a bicycle. To keep your balance, you must keep moving.",
            "Imagination is more important than knowledge. Knowledge is limited. Imagination encircles the world.",
        ],
    },
    {
        "name": "Emily Dickinson",
        "citations": [
            "We never know how high we are till we are called to rise. Then if we are true to form our statures touch the skies.",
            "Truth is such a rare thing, it is delighted to tell it.",
            "The soul should always stand ajar, ready to welcome the ecstatic experience.",
        ],
    },
    {
        "name": "Maya Angelou",
        "citations": [
            "I've learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel.",
            "You will face many defeats in life, but never let yourself be defeated.",
            "If you don't like something, change it. If you can't change it, change your attitude.",
            "Nothing can dim the light which shines from within.",
        ],
    },
    {
        "name": "Lao Tzu",
        "citations": [
            "Silence is a source of great strength.",
            "If you are depressed, you are living in the past. If you are anxious, you are living in the future. if you are at peace, you are living in the present.",
            "Be content with what you have, rejoice in the way things are. When you realize there is nothing lacking, the whole world belongs to you.",
            "Care about what other people think and you will always be their prisoner."
        ]
    },
    {
        "name": "Henry Ford",
        "citations": [
            "Most people spend more time and energy going around problems than in trying to solve them.",
            "If you always do what you've always done, you'll always get what you've always got.",
            "Coming together is a beginning, staying together is progress, and working together is success.",
            "Thinking is the hardest work there is, which is probably the reason why so few engage in it."
        ]
    },
    {
        "name": "Aristophanes",
        "citations": [
            "Even if you persuade me, you won't persuade me.",
            "You cannot teach a crab to walk straight.",
            "Youth ages, immaturity is outgrown, ignorance can be educated, and drunkenness sobered, but stupid lasts forever.",
            "Love is merely the name for the desire and pursuit of the whole."
        ]
    },
    {
        "name": "Bruce Lee",
        "citations": [
            "In the middle of chaos lies opportunity.",
            "We can see through others only when we can see through ourselves.",
            "A wise man can learn more from a foolish question than a fool can learn from a wise answer.",
            "As you think, so shall you become."
        ]
    },
    {
        "name": "Buddha",
        "citations": [
            "Your work is to discover your work and then, with all your heart, to give yourself to it.",
            "Do not look for a sanctuary in anyone except your self.",
            "Work out your own salvation. Do not depend on others.",
            "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment."
        ]
    },
    {
        "name": "Confucius",
        "citations": [
            "If you chase two rabbits, you catch none.",
            "It doesn't matter how slow you go, as long as you don't stop.",
            "Our greatest glory is not in never falling but in rising every time we fall.",
            "Life is really simple, but men insist on making it complicated."
        ]
    },
    {
        "name": "Carl Jung",
        "citations": [
            "We cannot change anything unless we accept it.",
            "I am not what happened to me, I am what I choose to become.",
            "No tree, it is said, can grow to heaven unless its roots reach down to hell.",
            "Thinking is difficult, that's why most people judge."
        ]
    },
    {
        "name": "Charles Darwin",
        "citations": [
            "A man who dares to waste one hour of time has not discovered the value of life.",
            "If the misery of the poor be caused not by the laws of nature, but by our institutions, great is our sin.",
            "We will now discuss in a little more detail the Struggle for Existence.",
            "The very essence of instinct is that it's followed independently of reason."
        ]
    },
    {
        "name": "Genghis Khan",
        "citations": [
            "There is no value in anything until it is finished.",
            "Even when a friend does something you do not like, he continues to be your friend.",
            "an action committed in anger is an action doomed to failure.",
            "If you're afraid - don't do it, - if you're doing it - don't be afraid!"
        ]
    },
    {
        "name": "Isaac Newton",
        "citations": [
            "To every action there is always opposed an equal reaction.",
            "What we know is a drop, what we don't know is an ocean.",
            "The best way to understanding is a few good examples.",
            "If I have seen further than others, it is by standing upon the shoulders of giants."
        ]
    },
    {
        "name": "Heraclitus",
        "citations": [
            "Man's character is his fate.",
            "Everything flows, nothing stands still.",
            "Much learning does not teach understanding.",
            "Abundance of knowledge does not teach men to be wise."
        ]
    },
    {
        "name": "Publilius Syrus",
        "citations": [
            "To do two things at once is to do neither.",
            "Debt is the slavery of the free.",
            "No man is happy unless he believes he is.",
            "From the errors of others, a wise man corrects his own."
        ]
    },
    {
        "name": "Nikola Tesla",
        "citations": [
            "Our virtues and our failings are inseparable, like force and matter. When they separate, man is no more.",
            "If you only knew the magnificence of the 3, 6, and 9, then you would have a key to the universe.",
            "It's not the love you make. It's the love you give.",
            "If you want to find the secrets of the universe, think in terms of energy, frequency and vibration."
        ]
    },
    {
        "name": "Paramahansa Yogananda",
        "citations": [
            "Remain calm, serene, always in command of yourself. You will then find out how easy it is to get along.",
            "If you cling to a certain thought with dynamic will power, it finally assumes a tangible outward form.",
            "The season of failure is the best time for sowing the seeds of success.",
            "Change yourself and you have done your part in changing the world."
        ]
    },
    {
        "name": "Herodotus",
        "citations": [
            "The destiny of man is in his own soul.",
            "Force has no place where there is need of skill.",
            "In peace, sons bury their fathers. In war, fathers bury their sons.",
            "Humans and prosperity never endure side by side for long."
        ]
    },
    {
        "name": "Alexander Graham Bell",
        "citations": [
            "Ideas do not reach perfection in a day, no matter how much study is put upon them.",
            "Before anything else, preparation is the key to success.",
            "When one door closes another door opens",
            "Night is a more quiet time to work. It aids thought."
        ]
    },
    {
        "name": "Anne Frank",
        "citations": [
            "In the long run, the sharpest weapon of all is a kind and gentle spirit.",
            "The dead receive more flowers than the living because regret is stronger than gratitude.",
            "Laziness may appear attractive, but work gives satisfaction.",
            "No one has ever become poor by giving."
        ]
    },
    {
        "name": "Aristotle",
        "citations": [
            "The whole is greater than the sum of its parts.",
            "We become brave by doing brave acts.",
            "The more you know, the more you know you don't know.",
            "To lead an orchestra, you must turn your back on the crowd."
        ]
    },
    {
        "name": "Brian Tracy",
        "citations": [
            "It doesn't matter where you are coming from. All that matters is where you are going.",
            "20 percent of your activities will account for 80 percent of your results.",
            "Everything you've ever wanted is on the other side of fear.",
            "The more reasons you have for achieving your goal, the more determined you will become."
        ]
    },
    {
        "name": "Benjamin Mays",
        "citations": [
            "The tragedy of life doesn't lie in not reaching your goal. The tragedy lies in having no goals to reach.",
            "You have the ability, now apply yourself.",
            "Whatever you do,strive to do it so well that no man living and no man dead and no man yet to be born could do it any better."
        ]
    },
    {
        "name": "Edgar Allan Poe",
        "citations": [
            "Invisible things are the only realities.",
            "Believe nothing you hear, and only one half that you see.",
            "Every poem should remind the reader that they are going to die.",
            "Never to suffer would never to have been blessed."
        ]
    },
    {
        "name": "Leonardo da Vinci",
        "citations": [
            "Time stays long enough for anyone who will use it.",
            "The greatest deception men suffer is from their own opinions.",
            "All our knowledge has its origins in our perceptions.",
            "He who possesses most must be most afraid of loss."
        ]
    },
    {
        "name": "Marcus Aurelius",
        "citations": [
            "Think of yourself as dead. you have lived your life. Now, take what's left, and live it properly.",
            "The best answer to anger is silence.",
            "A man's worth is no greater than his ambitions.",
            "Waste no more time arguing about what a good man should be. Be one."
        ]
    },
    {
        "name": "Martin Luther King, Jr.",
        "citations": [
            "If you can't fly, run. If you can't run, walk. If you can't walk, crawl, but by all means, keep moving.",
            "The time is always right to do what is right.",
            "If I cannot do great things. I can do small things in a great way.",
            "There can be no deep disappointment where there is not deep love."
        ]
    },
    {
        "name": "Morihei Ueshiba",
        "citations": [
            "When you lose your desire for things that do not matter, you will be free.",
            "Your heart is full of fertile seeds, waiting to sprout.",
            "Failure is the key to success; each mistake teaches us something.",
            "A good stance and posture reflect a proper state of mind."
        ]
    },
    {
        "name": "Mother Teresa",
        "citations": [
            "Yesterday is gone. Tomorrow has not yet come. We have only today.",
            "Do not wait for leaders; do it alone, person to person.",
            "It's not how much we give but how much love we put into giving.",
            "Kind words can be short and easy to speak, but their echoes are truly endless."
        ]
    },
    {
        "name": "Nelson Mandela",
        "citations": [
            "One of the most difficult things is not to change society - but to change yourself.",
            "You can start changing our world for the better daily, no matter how small the action.",
            "Live life as though nobody is watching, and express yourself as though everyone is listening.",
            "It always seems impossible until it's done."
        ]
    },
    {
        "name": "Nicolas Chamfort",
        "citations": [
            "Pleasure can be supported by an illusion; but happiness rests upon truth.",
            "Where violence reigns, reason is weak.",
            "The most wasted day of all is that on which we have not laughed.",
            "Public opinion is the worst of all opinions."
        ]
    },
    {
        "name": "Publilius Syrus",
        "citations": [
            "To do two things at once is to do neither.",
            "No man is happy unless he believes he is.",
            "From the errors of others, a wise man corrects his own.",
            "The greatest of empires, is the empire over one's self."
        ]
    },
    {
        "name": "Socrates",
        "citations": [
            "True knowledge exists in knowing that you know nothing.",
            "An un-examined life is not worth living.",
            "It is better to change an opinion than to persist in a wrong one.",
            "The world is a puzzle; no need to make sense out of it."
        ]
    },
    {
        "name": "Samuel Butler",
        "citations": [
            "Life is the art of drawing sufficient conclusions from insufficient premises.",
            "Logic is like the sword - those who appeal to it shall perish by it.",
            "To do great work one must be very idle as well as very industrious.",
            "All animals except man know that the principal business of life is to enjoy it."
        ]
    },
    {
        "name": "Steve Jobs",
        "citations": [
            "Don't let the noise of others' opinions drown out your own inner voice.",
            "Your time is limited, so don't waste it living someone elses. life",
            "The ones who are crazy enough to think they can change the world, are the ones that do.",
            "The people who are crazy enough to think they can change the world are the ones who do."
        ]
    },
    {
        "name": "Steve Harvey",
        "citations": [
            "Your gift is something that you can do innately better than anything else.",
            "Sometimes out of your biggest misery, comes your greatest gain.",
            "The number one cause of failure is the fear of failure.",
            "Your setback is just a setup for a comeback."
        ]
    },
    {
        "name": "Voltaire",
        "citations": [
            "The longer we dwell on our misfortunes, the greater is their power to harm us.",
            "Judge a man by his questions rather than his answers.",
            "Those who can make you believe absurdities can make you commit atrocities.",
            "It is difficult to free fools from the chains they revere."
        ]
    },
    {
        "name": "Winston Churchill",
        "citations": [
            "Continuous effort - not strength or intelligence - is the key to unlocking our potential.",
            "The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty.",
            "The power of man has grown in every sphere, except over himself.",
            "Success is not final, failure is not fatal: it is the courage to continue that counts."
        ]
    },
]

# Iterate over each author to create Author and Citation instances
for author_info in authors_info:
    author = Author(name=author_info["name"])
    db_storage.new(author)
    for citation_text in author_info["citations"]:
        citation = Citation(text=citation_text, author=author)
        db_storage.new(citation)

# Commit changes to the database
db_storage.save()

# Optionally, print the results to verify
print("Citations:")
all_citations = db_storage.all(Citation)
for citation in all_citations.values():
    print(f'{citation.text} - {citation.author.name}')

print("\nAuthors:")
all_authors = db_storage.all(Author)
for author in all_authors.values():
    print(author.name)

db_storage.close()