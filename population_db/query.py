#!/usr/bin/python3

from models.author import Author
from models.quote import Quote
from models.category import Category
from models.engine.db_storage import storage

def get_or_create_category(category_name):
    """Get an existing category or create a new one if it does not exist."""
    all_categories = storage.all(Category)
    for category_id, category_obj in all_categories.items():
        if category_obj.name == category_name:
            return category_obj
    new_category = Category(name=category_name)
    storage.new(new_category)
    storage.save()
    return new_category


Inspirational = get_or_create_category("Inspirational")
humor = get_or_create_category("Humor")
Motivational = get_or_create_category("Motivational")
wisdom = get_or_create_category("Wisdom")
love = get_or_create_category("Love")
life = get_or_create_category("Life")
Creativity = get_or_create_category("Creativity")
Hope = get_or_create_category("Hope")
Courage = get_or_create_category("Courage")
Leadership = get_or_create_category("Leadership")
Adventure = get_or_create_category("Adventure")
Happiness = get_or_create_category("Happiness")
Friendship = get_or_create_category("Friendship")
Dreams = get_or_create_category("Dreams")
Creativity = get_or_create_category("Creativity")
Kindness = get_or_create_category("Kindness")
Mindfulness = get_or_create_category("Mindfulness")
Gratitude = get_or_create_category("Gratitude")
Success = get_or_create_category("Success")
Perseverance = get_or_create_category("Perseverance")

Einstein = Author(name="Albert Einstein")
Cervantes = Author(name="Miguel de Cervantes")
Aristotle = Author(name="Aristotle")
Aristophanes = Author(name="Aristophanes")
Mandela = Author(name="Nelson Mandela")
Roosevelt = Author(name="Franklin D. Roosevelt")
Churchill = Author(name="Winston Churchill")
Maxwell = Author(name="John C. Maxwell")
Helen_Keller = Author(name="Helen Keller")
Lewis = Author(name="C.S. Lewis")
Marsha_Norman = Author(name="Marsha Norman")
Oscar_Wilde = Author(name="Oscar Wilde")
Emily_Dickinson = Author(name="Emily Dickinson")
Martin_Luther = Author(name="Martin Luther King, Jr.")
Oprah = Author(name="Oprah Winfrey")
Ernest_Hemingway = Author(name="Ernest Hemingway")
George_Eliot = Author(name="George Eliot")
Lao_Tzu = Author(name="Lao Tzu")
Mark_Twain = Author(name="Mark Twain")
Mahatma_Gandhi = Author(name="Mahatma Gandhi")
Amelia_Earhart = Author(name="Amelia Earhart")
George_Bernard_Shaw = Author(name="George Bernard Shaw")
Seth_Godin = Author(name="Seth Godin")
Steve_Jobs = Author(name="Steve Jobs")
Ronald_Reagan = Author(name="Ronald Reagan")
John_Quincy_Adams = Author(name="John Quincy Adams")
Douglas_MacArthur = Author(name="Douglas MacArthur")
Henry_David_Thoreau = Author(name="Henry David Thoreau")
William_Arthur_Ward = Author(name="William Arthur Ward")
Peter_Drucker = Author(name="Peter Drucker")
Sam_Levenson = Author(name="Sam Levenson")
Nikos_Kazantzakis = Author(name="Nikos Kazantzakis")
Wayne_Gretzky = Author(name="Wayne Gretzky")
Chris_Grosser = Author(name="Chris Grosser")
Charles_Kingsleigh = Author(name="Charles Kingsleigh")
Albert_Schweitzer = Author(name="Albert Schweitzer")
Vidal_Sassoon = Author(name="Vidal Sassoon")
Bo_Bennett = Author(name="Bo Bennett")
Lionel_Hampton = Author(name="Lionel Hampton")
Henry_Ward_Beecher = Author(name="Henry Ward Beecher")
Zig_Ziglar = Author(name="Zig Ziglar")
Melody_Beattie = Author(name="Melody_Beattie")
Colin_R_Davis = Author(name="Colin R. Davis")
Vidal_Sassoon = Author(name="Vidal Sassoon")
Aesop = Author(name="Aesop")
Dalai_Lama = Author(name="Dalai Lama")
Robert_Green_Ingersoll = Author(name="Robert Green Ingersoll")
Amelia_Barr = Author(name="Amelia Barr")
Paramahansa_Yogananda = Author(name="Paramahansa Yogananda")
Raktivist = Author(name="Raktivist")
Ashleigh_Brilliant = Author(name="Ashleigh Brilliant")
Johann_Wolfgang_von_Goethe = Author(name="Johann Wolfgang von Goethe")
Richard_Aldington = Author(name="Richard Aldington")
John_Amatt = Author(name="John Amatt")
J_M_Barrie = Author(name="J.M. Barrie")
Joseph_Campbell = Author(name="Joseph Campbell")
A_A_Milne = Author(name="A.A. Milne")
John_F_Kennedy = Author(name="John F. Kennedy")
Ralph_Nader = Author(name="Ralph Nader")
Arnold_H_Glasow = Author(name="Arnold H. Glasow")
Warren_Bennis = Author(name="Warren Bennis")
Simon_Sinek = Author(name="Simon Sinek")
Grace_Murray_Hopper = Author(name="Grace Murray Hopper")
Tom_Bradley = Author(name="Tom Bradley")
James_Dean = Author(name="James Dean")
Tupac_Shakur = Author(name="Tupac Shakur")
Langston_Hughes = Author(name="Langston Hughes")
Anatole_France = Author(name="Anatole France")
Colin_Powell = Author(name="Colin Powell")
Norman_Vaughan = Author(name="Norman Vaughan")
George_Lucas = Author(name="George Lucas")
Henri_Matisse = Author(name="Henri Matisse")
Maya_Angelou = Author(name="Maya Angelou")
William_Plomer = Author(name="William Plomer")
Pablo_Picasso = Author(name="Pablo Picasso")
Jack_London = Author(name="Jack London")
Dieter_F_Uchtdorf = Author(name="Dieter F. Uchtdorf")
Eric_Hoffer = Author(name="Eric Hoffer")
Osho = Author(name="Osho")
Friedrich_Nietzsche = Author(name="Friedrich Nietzsche")
Scott_Adams = Author(name="Scott Adams")
Ralph_Waldo_Emerson = Author(name="Ralph Waldo Emerson")
Charles_Mingus = Author(name="Charles Mingus")
Edwin_Land = Author(name="Edwin Land")
Ursula_K_Le_Guin = Author(name="Ursula K. Le Guin")
Socrates = Author(name="Socrates")
Confucius = Author(name="Confucius")
Abraham_Lincoln = Author(name="Abraham Lincoln")
Buddha = Author(name="Buddha")
Plato = Author(name="Plato")
Edmund_Burke = Author(name="Edmund Burke")
Charles_R_Swindoll = Author(name="Charles R. Swindoll")
Bethany_Hamilton = Author(name="Bethany Hamilton")
E_E_Cummings = Author(name="E.E. Cummings")
Walt_Disney = Author(name="Walt Disney")
Ralph_Marston = Author(name="Ralph Marston")
Goldie_Hawn = Author(name="Goldie Hawn")
John_Lennon = Author(name="John Lennon")
Audrey_Hepburn = Author(name="Audrey Hepburn")
Marcus_Aurelius = Author(name="Marcus Aurelius")
Ayn_Rand = Author(name="Ayn Rand")
George_Sand = Author(name="George Sand")
Rabindranath_Tagore = Author(name="Rabindranath Tagore")
Victor_Hugo = Author(name="Victor Hugo")
Nicholas_Sparks = Author(name="Nicholas Sparks")
T_Tolis = Author(name="T. Tolis")
Antoine_de_Saint_Exupéry = Author(name="Antoine de Saint-Exupéry")
Dr_Seuss = Author(name="Dr. Seuss")
Max_Muller = Author(name="Max Muller")
Thomas_A_Edison = Author(name="Thomas A. Edison")
Walter_Elliot = Author(name="Walter Elliot")
Vince_Lombardi = Author(name="Vince Lombardi")
Newt_Gingrich = Author(name="Newt Gingrich")
Thomas_Fowell_Buxton = Author(name="Thomas Fowell Buxton")
Julie_Andrews = Author(name="Julie Andrews")
Og_Mandino = Author(name="Og Mandino")
Tom_Hopkins = Author(name="Tom Hopkins")
Thich_Nhat_Hanh = Author(name="Thich Nhat Hanh")
Amit_Ray = Author(name="Amit Ray")
Sharon_Salzberg = Author(name="Sharon Salzberg")
Jon_Kabat_Zinn = Author(name="Jon Kabat-Zinn")
Alan_Watts = Author(name="Alan Watts")
Eckhart_Tolle = Author(name="Eckhart Tolle")
Henry_Miller = Author(name="Henry Miller")
Deepak_Chopra = Author(name="Deepak Chopra")
Desmond_Tutu = Author(name="Desmond Tutu")
Walt_Whitman = Author(name="Walt Whitman")
J_R_R_Tolkien = Author(name="J.R.R. Tolkien")
Maxine_Hong_Kingston = Author(name="Maxine Hong Kingston")
Christopher_Reeve = Author(name="Christopher Reeve")
Michelle_Horst = Author(name="Michelle Horst")
Charles_H_Spurgeon = Author(name="Charles H. Spurgeon")
Anne_Lamott = Author(name="Anne Lamott")
Epicurus = Author(name="Epicurus")
Michelle_Obama = Author(name="Michelle Obama")
Samuel_Smiles = Author(name="Samuel Smiles")
Orison_Swett_Marden = Author(name="Orison Swett Marden")
Elbert_Hubbard = Author(name="Elbert Hubbard")
Woodrow_Wilson = Author(name="Woodrow Wilson")
David_Tyson = Author(name="David Tyson")
Ed_Cunningham = Author(name="Ed Cunningham")
Khalil_Gibran = Author(name="Khalil Gibran")
Walter_Winchell = Author(name="Walter Winchell")
Jean_de_La_Fontaine = Author(name="Jean de La Fontaine")
Henry_Van_Dyke = Author(name="Henry Van Dyke")
William_Shakespeare = Author(name="William Shakespeare")
Cicero = Author(name="Cicero")
Elie_Wiesel = Author(name="Elie Wiesel")
Jim_Morrison = Author(name="Jim Morrison")
Alexander_Dumas = Author(name="Alexander Dumas")
Baltasar_Gracián = Author(name="Baltasar Gracián")
George_Washington = Author(name="George Washington")

authors = [Churchill, Roosevelt, Mandela, Einstein, Cervantes, Aristotle, Aristophanes, Maxwell, 
           Helen_Keller, Martin_Luther, Lewis, Marsha_Norman, Oscar_Wilde, George_Eliot, 
           Lao_Tzu, Emily_Dickinson, Oprah, Ernest_Hemingway, Mark_Twain, Mahatma_Gandhi,
           Amelia_Earhart, Johann_Wolfgang_von_Goethe, George_Bernard_Shaw, Seth_Godin,
           Steve_Jobs, Ronald_Reagan, John_Quincy_Adams, Douglas_MacArthur, Henry_David_Thoreau,
           William_Arthur_Ward, Peter_Drucker, Sam_Levenson, Nikos_Kazantzakis, Wayne_Gretzky,
           Chris_Grosser, Charles_Kingsleigh, Albert_Schweitzer, Vidal_Sassoon, Bo_Bennett,
           Lionel_Hampton, Henry_Ward_Beecher, Zig_Ziglar, Melody_Beattie, Colin_R_Davis,
           Vidal_Sassoon, Aesop, Dalai_Lama, Robert_Green_Ingersoll, Amelia_Barr,
           Paramahansa_Yogananda, Raktivist, Ashleigh_Brilliant,
           Richard_Aldington, J_M_Barrie, Joseph_Campbell, A_A_Milne, John_F_Kennedy,
           Ralph_Nader, Arnold_H_Glasow, Warren_Bennis, Simon_Sinek, Grace_Murray_Hopper,
           Tom_Bradley, James_Dean, Tupac_Shakur, Langston_Hughes, Anatole_France, 
           Colin_Powell, Norman_Vaughan, George_Lucas, Henri_Matisse, Maya_Angelou,
           William_Plomer, Pablo_Picasso, Jack_London, Dieter_F_Uchtdorf, Eric_Hoffer,
           Osho, Friedrich_Nietzsche, Scott_Adams, Ralph_Waldo_Emerson, Charles_Mingus,
           Edwin_Land, Ursula_K_Le_Guin, Socrates, Confucius, Abraham_Lincoln, Buddha,
           Plato, Edmund_Burke, Charles_R_Swindoll, Bethany_Hamilton, E_E_Cummings,
           Walt_Disney, Ralph_Marston, Goldie_Hawn, John_Lennon, Audrey_Hepburn, 
           Marcus_Aurelius, Ayn_Rand, George_Sand, Rabindranath_Tagore, Victor_Hugo,
           Nicholas_Sparks, T_Tolis, Antoine_de_Saint_Exupéry, Dr_Seuss, Max_Muller,
           Thomas_A_Edison, Walter_Elliot, Vince_Lombardi,Newt_Gingrich, Thomas_Fowell_Buxton,
           Julie_Andrews, Og_Mandino, Tom_Hopkins, Thich_Nhat_Hanh, Amit_Ray, Sharon_Salzberg,
           Jon_Kabat_Zinn, Alan_Watts, Eckhart_Tolle, Henry_Miller, Deepak_Chopra, Desmond_Tutu, 
           Walt_Whitman, J_R_R_Tolkien, Maxine_Hong_Kingston, Christopher_Reeve, Michelle_Horst,
           Charles_H_Spurgeon, Anne_Lamott, Epicurus, Michelle_Obama, Samuel_Smiles, Orison_Swett_Marden, 
           Elbert_Hubbard, Woodrow_Wilson, David_Tyson, Ed_Cunningham, Khalil_Gibran, Walter_Winchell, 
           Jean_de_La_Fontaine, Henry_Van_Dyke, William_Shakespeare, Cicero, Elie_Wiesel, Jim_Morrison,
           Alexander_Dumas, Baltasar_Gracián, ]
for author in authors:
    storage.new(author)


quotes_data = [
    {"text": "Imagination is more important than knowledge.", "author": Einstein, "category": Inspirational},
    {"text": "Knowing yourself is the beginning of all wisdom.", "author": Aristotle, "category": wisdom},
    {"text": "The course of true love never did run smooth.", "author": Aristophanes, "category": love},
    {"text": "It always seems impossible until it's done.", "author": Mandela, "category": Motivational},
    {"text": "Life is what happens when you're busy making other plans.", "author": Cervantes, "category": life},
    {"text": "In the middle of difficulty lies opportunity.", "author": Einstein, "category": Inspirational},
    {"text": "We cannot solve problems with the kind of thinking we employed when we came up with them.", "author": Einstein, "category": wisdom},
    {"text": "The greatest glory in living lies not in never falling, but in rising every time we fall.", "author": Mandela, "category": Inspirational},
    {"text": "To be content with little is hard; to be content with much, impossible.", "author": Aristotle, "category": life},
    {"text": "Creativity is intelligence having fun.", "author": Einstein, "category": Creativity},
    {"text": "Creativity is contagious. Pass it on.", "author": Einstein, "category": Creativity},
    {"text": "The secret to creativity is knowing how to hide your sources.", "author": Einstein, "category": Creativity},
    {"text": "The only limit to our realization of tomorrow will be our doubts of today.", "author": Roosevelt, "category": Motivational},
    {"text": "The only limit to our realization of tomorrow is our doubts of today.", "author": Roosevelt, "category": Inspirational},
    {"text": "The only thing we have to fear is fear itself.", "author": Roosevelt, "category": wisdom},
    {"text": "It is the mark of an educated mind to be able to entertain a thought without accepting it.", "author": Aristotle, "category": wisdom},
    {"text": "Love is composed of a single soul inhabiting two bodies.", "author": Aristotle, "category": love},
    {"text": "Hope is a waking dream.", "author": Aristotle, "category": Hope},
    {"text": "Courage is not the absence of fear, but the triumph over it.", "author": Mandela, "category": Courage},
    {"text": "Success is not final, failure is not fatal: It is the courage to continue that counts.", "author": Churchill, "category": Motivational},
    {"text": "Success consists of going from failure to failure without loss of enthusiasm.", "author": Churchill, "category": Motivational},
    {"text": "Courage is what it takes to stand up and speak; courage is also what it takes to sit down and listen.", "author": Churchill, "category": Courage},
    {"text": "The price of greatness is responsibility.", "author": Churchill, "category": Leadership},
    {"text": "A leader is one who knows the way, goes the way, and shows the way.", "author": Maxwell, "category": Leadership},
    {"text": "Leadership is not about titles, positions, or flowcharts. It is about one life influencing another.", "author": Maxwell, "category": Leadership},
    {"text": "Life is either a daring adventure or nothing at all.", "author": Helen_Keller, "category": Adventure},
    {"text": "The best and most beautiful things in the world cannot be seen or even touched. They must be felt with the heart.", "author": Helen_Keller, "category": Happiness},
    {"text": "Walking with a friend in the dark is better than walking alone in the light.", "author": Helen_Keller, "category": Friendship},
    {"text": "You are never too old to set another goal or to dream a new dream.", "author": Lewis, "category": Motivational},
    {"text": "Friendship is born at that moment when one person says to another, 'What! You too? I thought I was the only one.", "author": Lewis, "category": Friendship},
    {"text": "Dreams are illustrations... from the book your soul is writing about you.", "author": Marsha_Norman, "category": Dreams},
    {"text": "Art is the most intense mode of individualism that the world has known.", "author": Oscar_Wilde, "category": Creativity},
    {"text": "Hope is the thing with feathers that perches in the soul - and sings the tunes without the words - and never stops at all.", "author": Emily_Dickinson, "category": Hope},
    {"text": "We must accept finite disappointment, but never lose infinite hope.", "author": Martin_Luther, "category": Hope},
    {"text": "A genuine leader is not a searcher for consensus but a molder of consensus.", "author": Martin_Luther, "category": Leadership},
    {"text": "The biggest adventure you can take is to live the life of your dreams.", "author": Oprah, "category": Adventure},
    {"text": "Every man's life ends the same way. It is only the details of how he lived and how he died that distinguish one man from another.", "author": Ernest_Hemingway, "category": Adventure},
    {"text": "Friendship is the inexpressible comfort of feeling safe with a person, having neither to weigh thoughts nor measure words.", "author": George_Eliot, "category": Friendship},
    {"text": "It is never too late to be what you might have been.", "author": George_Eliot, "category": Adventure},
    {"text": "Adventure is not outside man; it is within.", "author": George_Eliot, "category": Adventure},
    {"text": "The journey of a thousand miles begins with one step.", "author": Lao_Tzu, "category": wisdom},
    {"text": "Being deeply loved by someone gives you strength, while loving someone deeply gives you courage.", "author": Lao_Tzu, "category": love},
    {"text": "Kindness in words creates confidence. Kindness in thinking creates profoundness. Kindness in giving creates love.", "author": Lao_Tzu, "category": Kindness},
    {"text": "The best way to cheer yourself up is to try to cheer somebody else up.", "author": Mark_Twain, "category": Happiness},
    {"text": "Kindness is a language which the deaf can hear and the blind can see.", "author": Mark_Twain, "category": Kindness},
    {"text": "You must be the change you wish to see in the world.", "author": Mahatma_Gandhi, "category": wisdom},
    {"text": "The simplest acts of kindness are by far more powerful then a thousand heads bowing in prayer.", "author": Mahatma_Gandhi, "category": Kindness},
    {"text": "The best way to find yourself is to lose yourself in the service of others.", "author": Mahatma_Gandhi, "category": Kindness},
    {"text": "A single act of kindness throws out roots in all directions, and the roots spring up and make new trees.", "author": Amelia_Earhart, "category": Kindness},
    {"text": "Whatever you do, or dream you can, begin it. Boldness has genius and power and magic in it.", "author": Johann_Wolfgang_von_Goethe, "category": Dreams},
    {"text": "Imagination is the beginning of creation. You imagine what you desire, you will what you imagine, and at last, you create what you will.", "author": George_Bernard_Shaw, "category": Creativity},
    {"text": "You see things; and you say, 'Why?' But I dream things that never were; and I say, 'Why not?'", "author": George_Bernard_Shaw, "category": Dreams},
    {"text": "The only thing worse than starting something and failing... is not starting something.", "author": Seth_Godin, "category": Dreams},
    {"text": "Leadership is the art of giving people a platform for spreading ideas that work.", "author": Seth_Godin, "category": Leadership},
    {"text": "When you realize nothing is lacking, the whole world belongs to you.", "author": Lao_Tzu, "category": Mindfulness},
    {"text": "A leader is best when people barely know he exists, when his work is done, his aim fulfilled, they will say: we did it ourselves.", "author": Lao_Tzu, "category": Leadership},
    {"text": "The only way to do great work is to love what you do.", "author": Steve_Jobs, "category": Motivational},
    {"text": "Innovation distinguishes between a leader and a follower.", "author": Steve_Jobs, "category": Creativity},
    {"text": "Creativity is just connecting things.", "author": Steve_Jobs, "category": Creativity},
    {"text": "The greatest leader is not necessarily the one who does the greatest things. He is the one that gets the people to do the greatest things.", "author": Ronald_Reagan, "category": Creativity},
    {"text": "If your actions inspire others to dream more, learn more, do more and become more, you are a leader.", "author": John_Quincy_Adams, "category": Leadership},
    {"text": "A true leader has the confidence to stand alone, the courage to make tough decisions, and the compassion to listen to the needs of others. He does not set out to be a leader, but becomes one by the equality of his actions and the integrity of his intent.", "author": Douglas_MacArthur, "category": Leadership},
    {"text": "It's not what you look at that matters, it's what you see.", "author": Henry_David_Thoreau, "category": Motivational},
    {"text": "You must live in the present, launch yourself on every wave, find your eternity in each moment. Fools stand on their island of opportunities and look toward another land. There is no other land; there is no other life but this.", "author": Henry_David_Thoreau, "category": Mindfulness},
    {"text": "The language of friendship is not words but meanings.", "author": Henry_David_Thoreau, "category":Friendship},
    {"text": "Dreams are the touchstones of our characters.", "author": Henry_David_Thoreau, "category": Dreams},
    {"text": "Feeling gratitude and not expressing it is like wrapping a present and not giving it.", "author": William_Arthur_Ward, "category": Gratitude},
    {"text": "The mediocre teacher tells. The good teacher explains. The superior teacher demonstrates. The great teacher inspires.", "author": William_Arthur_Ward, "category": Leadership},
    {"text": "The best way to predict the future is to create it.", "author": Peter_Drucker, "category": Motivational},
    {"text": "Management is doing things right; leadership is doing the right things.", "author": Peter_Drucker, "category": Leadership},
    {"text": "Don't watch the clock; do what it does. Keep going.", "author": Sam_Levenson, "category": Inspirational},
    {"text": "In order to succeed, we must first believe that we can.", "author": Nikos_Kazantzakis, "category": Inspirational},
    {"text": "You miss 100% of the shots you don't take.", "author": Wayne_Gretzky, "category": Motivational},
    {"text": "Opportunities don't happen, you create them.", "author": Chris_Grosser, "category": Motivational},
    {"text": "The only way to achieve the impossible is to believe it is possible.", "author": Charles_Kingsleigh, "category": Motivational},
    {"text": "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful.", "author": Albert_Schweitzer, "category": Success},
    {"text": "The only place where success comes before work is in the dictionary.", "author": Vidal_Sassoon, "category": Success},
    {"text": "Success is not in what you have, but who you are.", "author": Bo_Bennett, "category": Success},
    {"text": "Gratitude is when memory is stored in the heart and not in the mind.", "author": Lionel_Hampton, "category": Gratitude},
    {"text": "Gratitude is the fairest blossom which springs from the soul.", "author": Henry_Ward_Beecher, "category": Gratitude},
    {"text": "Gratitude is the healthiest of all human emotions. The more you express gratitude for what you have, the more likely you will have even more to express gratitude for.", "author": Zig_Ziglar, "category": Gratitude},
    {"text": "Gratitude unlocks the fullness of life. It turns what we have into enough, and more. It turns denial into acceptance, chaos to order, confusion to clarity. It can turn a meal into a feast, a house into a home, a stranger into a friend.", "author": Melody_Beattie, "category": Gratitude},
    {"text": "The road to success and the road to failure are almost exactly the same.", "author": Colin_R_Davis, "category": Motivational},
    {"text": "The only place where success comes before work is in the dictionary.", "author": Vidal_Sassoon, "category": Motivational},
    {"text": "No act of kindness, no matter how small, is ever wasted.", "author": Aesop, "category": Kindness},
    {"text": "The purpose of our lives is to be happy.", "author": Dalai_Lama, "category": Happiness},
    {"text": "Happiness is not something ready-made. It comes from your own actions.", "author": Dalai_Lama, "category": Happiness},
    {"text": "Be kind whenever possible. It is always possible.", "author": Dalai_Lama, "category": Kindness},
    {"text": "Kindness is the sunshine in which virtue grows.", "author": Robert_Green_Ingersoll, "category": Kindness},
    {"text": "Kindness is always fashionable, and always welcome.", "author": Amelia_Barr, "category": Kindness},
    {"text": "Kindness is the light that dissolves all walls between souls, families, and nations.", "author": Paramahansa_Yogananda, "category": Kindness},
    {"text": "Kindness is the ability to know what the right thing to do is and having the courage to do it!!", "author": Raktivist, "category": Kindness},
    {"text": "Be kind to unkind people, they need it the most.", "author": Ashleigh_Brilliant, "category": Kindness},
    {"text": "Kindness is the golden chain by which society is bound together.", "author": Johann_Wolfgang_von_Goethe, "category": Kindness},
    {"text": "Adventure is allowing the unexpected to happen to you. Exploration is experiencing what you have not experienced before.", "author": Richard_Aldington, "category": Adventure},
    {"text": "Adventure isn't hanging off a rope on the side of a mountain. Adventure is an attitude that we must apply to the day to day obstacles in life.", "author": John_Amatt, "category": Adventure},
    {"text": "To live would be an awfully big adventure.", "author": J_M_Barrie, "category": Adventure},
    {"text": "The only question in life is whether or not you are going to answer a hearty 'YES!' to your adventure.", "author": Joseph_Campbell, "category": Adventure},
    {"text": "You are braver than you believe, stronger than you seem, and smarter than you think.", "author": A_A_Milne, "category": Adventure},
    {"text": "Leadership and learning are indispensable to each other.", "author": John_F_Kennedy, "category": Leadership},
    {"text": "The function of leadership is to produce more leaders, not more followers.", "author": Ralph_Nader, "category": Leadership},
    {"text": "A good leader takes a little more than his share of the blame, a little less than his share of the credit.", "author": Arnold_H_Glasow, "category": Leadership},
    {"text": "Leadership is the capacity to translate vision into reality.", "author": Warren_Bennis, "category": Leadership},
    {"text": "Leadership is not about being in charge. It is about taking care of those in your charge.", "author": Simon_Sinek, "category": Leadership},
    {"text": "You manage things; you lead people.", "author": Grace_Murray_Hopper, "category": Leadership},
    {"text": "A dreamer is one who can only find his way by moonlight, and his punishment is that he sees the dawn before the rest of the world.", "author": Oscar_Wilde, "category": Dreams},
    {"text": "The only thing that will stop you from fulfilling your dreams is you.", "author": Tom_Bradley, "category": Dreams},
    {"text": "Dream as if you'll live forever, live as if you'll die today.", "author": James_Dean, "category": Dreams},
    {"text": "Reality is wrong. Dreams are for real.", "author": Tupac_Shakur, "category": Dreams},
    {"text": "Hold fast to dreams, for if dreams die, life is a broken-winged bird that cannot fly.", "author": Langston_Hughes, "category": Dreams},
    {"text": "To accomplish great things, we must not only act, but also dream, not only plan, but also believe.", "author": Anatole_France, "category": Dreams},
    {"text": "A dream doesn't become reality through magic; it takes sweat, determination and hard work.", "author": Colin_Powell, "category": Dreams},
    {"text": "Dream big and dare to fail.", "author": Norman_Vaughan, "category": Dreams},
    {"text": "Dreams are extremely important. You can't do it unless you imagine it.", "author": George_Lucas, "category": Dreams},
    {"text": "Creativity takes courage.", "author": Henri_Matisse, "category": Creativity},
    {"text": "You can't use up creativity. The more you use, the more you have.", "author": Maya_Angelou, "category": Creativity},
    {"text": "Creativity is the power to connect the seemingly unconnected.", "author": William_Plomer, "category": Creativity},
    {"text": "The chief enemy of creativity is 'good' sense.", "author": Pablo_Picasso, "category": Creativity},
    {"text": "You can't wait for inspiration, you have to go after it with a club.", "author": Jack_London, "category": Creativity},
    {"text": "The desire to create is one of the deepest yearnings of the human soul.", "author": Dieter_F_Uchtdorf, "category": Creativity},
    {"text": "Creativity is the ability to introduce order into the randomness of nature.", "author": Eric_Hoffer, "category": Creativity},
    {"text": "To be creative means to be in love with life. You can be creative only if you love life enough that you want to enhance its beauty, you want to bring a little more music to it, a little more poetry to it, a little more dance to it.", "author": Osho, "category": Creativity},
    {"text": "You need chaos in your soul to give birth to a dancing star.", "author": Friedrich_Nietzsche, "category": Creativity},
    {"text": "Creativity is allowing yourself to make mistakes. Art is knowing which ones to keep.", "author": Scott_Adams, "category": Creativity},
    {"text": "Every artist was first an amateur.", "author": Ralph_Waldo_Emerson, "category": Creativity},
    {"text": "What lies behind us and what lies before us are tiny matters compared to what lies within us.", "author": Ralph_Waldo_Emerson, "category": wisdom},
    {"text": "The only way to have a friend is to be one.", "author": Ralph_Waldo_Emerson, "category": Friendship},
    {"text": "Creativity is more than just being different. Anybody can plan weird; that's easy. What's hard is to be as simple as Bach. Making the simple, awesomely simple, that's creativity.", "author": Charles_Mingus, "category": Creativity},
    {"text": "An essential aspect of creativity is not being afraid to fail.", "author": Edwin_Land, "category": Creativity},
    {"text": "The creative adult is the child who survived.", "author": Ursula_K_Le_Guin, "category": Creativity},
    {"text": "The only true wisdom is in knowing you know nothing.", "author": Socrates, "category": wisdom},
    {"text": "Life is really simple, but we insist on making it complicated.", "author": Confucius, "category": wisdom},
    {"text": "It does not matter how slowly you go as long as you do not stop.", "author": Confucius, "category": Courage},
    {"text": "In the end, it's not the years in your life that count. It's the life in your years.", "author": Abraham_Lincoln, "category": wisdom},
    {"text": "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment.", "author": Buddha, "category": wisdom},
    {"text": "The mind is everything. What you think you become.", "author": Buddha, "category": wisdom},
    {"text": "We can easily forgive a child who is afraid of the dark; the real tragedy of life is when men are afraid of the light.", "author": Plato, "category": wisdom},
    {"text": "Life is not measured by the number of breaths we take, but by the moments that take our breath away.", "author": Maya_Angelou, "category": wisdom},
    {"text": "The only thing necessary for the triumph of evil is for good men to do nothing.", "author": Edmund_Burke, "category": wisdom},
    {"text": "Life is 10% what happens to us and 90% how we react to it.", "author": Charles_R_Swindoll, "category": Courage},
    {"text": "Courage doesn't mean you don't get afraid. Courage means you don't let fear stop you.", "author": Bethany_Hamilton, "category": Courage},
    {"text": "It takes courage to grow up and become who you really are.", "author": E_E_Cummings, "category": Courage},
    {"text": "All our dreams can come true, if we have the courage to pursue them.", "author": Walt_Disney, "category": Courage},
    {"text": "Happiness is a choice, not a result. Nothing will make you happy until you choose to be happy.", "author": Ralph_Marston, "category": Happiness},
    {"text": "The only thing that will make you happy is being happy with who you are, and not who people think you are.", "author": Goldie_Hawn, "category": Happiness},
    {"text": "Count your age by friends, not years. Count your life by smiles, not tears.", "author": John_Lennon, "category": Happiness},
    {"text": "The most important thing is to enjoy your life—to be happy—it's all that matters.", "author": Audrey_Hepburn, "category": Happiness},
    {"text": "The best thing to hold onto in life is each other.", "author": Audrey_Hepburn, "category": love},
    {"text": "The happiness of your life depends upon the quality of your thoughts.", "author": Marcus_Aurelius, "category": Happiness},
    {"text": "Learn to value yourself, which means: fight for your happiness.", "author": Ayn_Rand, "category": Happiness},
    {"text": "There is only one happiness in this life, to love and be loved.", "author": George_Sand, "category": Happiness},
    {"text": "When you arise in the morning, think of what a precious privilege it is to be alive - to breathe, to think, to enjoy, to love.", "author": Marcus_Aurelius, "category": Mindfulness},
    {"text": "Love is an endless mystery, for it has nothing else to explain it.", "author": Rabindranath_Tagore, "category": love},
    {"text": "The greatest happiness of life is the conviction that we are loved; loved for ourselves, or rather, loved in spite of ourselves.", "author": Victor_Hugo, "category": love},
    {"text": "Perseverance, secret of all triumphs.", "author": Victor_Hugo, "category": Perseverance},
    {"text": "Love is like the wind, you can't see it but you can feel it.", "author": Nicholas_Sparks, "category": love},
    {"text": "To love is nothing. To be loved is something. But to love and be loved, that’s everything.", "author": T_Tolis, "category": love},
    {"text": "Love is not just looking at each other, it's looking in the same direction.", "author": Antoine_de_Saint_Exupéry, "category": love},
    {"text": "You know you're in love when you can't fall asleep because reality is finally better than your dreams.", "author": Dr_Seuss, "category": love},
    {"text": "A flower cannot blossom without sunshine, and man cannot live without love.", "author": Max_Muller, "category": love},
    {"text": "Many of life's failures are people who did not realize how close they were to success when they gave up.", "author": Thomas_A_Edison, "category": Perseverance},
    {"text": "Perseverance is not a long race; it is many short races one after the other.", "author": Walter_Elliot, "category": Perseverance},
    {"text": "The difference between a successful person and others is not a lack of strength, not a lack of knowledge, but rather a lack in will.", "author": Vince_Lombardi, "category": Perseverance},
    {"text": "It's not whether you get knocked down. It's whether you get up.", "author": Vince_Lombardi, "category": Perseverance},
    {"text": "Perseverance is the hard work you do after you get tired of doing the hard work you already did.", "author": Newt_Gingrich, "category": Perseverance},
    {"text": "With ordinary talent and extraordinary perseverance, all things are attainable.", "author": Thomas_Fowell_Buxton, "category": Perseverance},
    {"text": "Perseverance is failing nineteen times and succeeding the twentieth.", "author": Julie_Andrews, "category": Perseverance},
    {"text": "I will persist until I succeed.", "author": Og_Mandino, "category": Perseverance},
    {"text": "I am not judged by the number of times I fail, but by the number of times I succeed: and the number of times I succeed is in direct proportion to the number of times I fail and keep trying.", "author": Tom_Hopkins, "category": Perseverance},
    {"text": "The present moment is the only moment available to us, and it is the door to all moments.", "author": Thich_Nhat_Hanh, "category": Mindfulness},
    {"text": "Smile, breathe, and go slowly.", "author": Thich_Nhat_Hanh, "category": Mindfulness},
    {"text": "Feelings come and go like clouds in a windy sky. Conscious breathing is my anchor.", "author": Thich_Nhat_Hanh, "category": Mindfulness},
    {"text": "The most precious gift we can offer anyone is our attention. When mindfulness embraces those we love, they will bloom like flowers.", "author": Thich_Nhat_Hanh, "category": Mindfulness},
    {"text": "Breathing in, I calm body and mind. Breathing out, I smile. Dwelling in the present moment I know this is the only moment.", "author": Thich_Nhat_Hanh, "category": Mindfulness},
    {"text": "Drink your tea slowly and reverently, as if it is the axis on which the world earth revolves – slowly, evenly, without rushing toward the future.", "author": Thich_Nhat_Hanh, "category": Mindfulness},
    {"text": "With mindfulness, you can establish yourself in the present in order to touch the wonders of life that are available in that moment.", "author": Thich_Nhat_Hanh, "category": Mindfulness},
    {"text": "Hope is important because it can make the present moment less difficult to bear. If we believe that tomorrow will be better, we can bear a hardship today.", "author": Thich_Nhat_Hanh, "category": Hope},
    {"text": "If you want to conquer the anxiety of life, live in the moment, live in the breath.", "author": Amit_Ray, "category": Mindfulness},
    {"text": "Mindfulness isn’t difficult, we just need to remember to do it.", "author": Sharon_Salzberg, "category": Mindfulness},
    {"text": "Mindfulness is about being fully awake in our lives. It is about perceiving the exquisite vividness of each moment. We also gain immediate access to our own powerful inner resources for insight, transformation, and healing.", "author": Jon_Kabat_Zinn, "category": Mindfulness},
    {"text": "This is the real secret of life - to be completely engaged with what you are doing in the here and now. And instead of calling it work, realize it is play.", "author": Alan_Watts, "category": Mindfulness},
    {"text": "In today’s rush, we all think too much — seek too much — want too much — and forget about the joy of just being.", "author": Eckhart_Tolle, "category": Mindfulness},
    {"text": "Realize deeply that the present moment is all you ever have. Make the Now the primary focus of your life.", "author": Eckhart_Tolle, "category": Mindfulness},
    {"text": "Wherever you are, be there totally.", "author": Eckhart_Tolle, "category": Mindfulness},
    {"text": "The moment one gives close attention to anything, even a blade of grass, it becomes a mysterious, awesome, indescribably magnificent world in itself.", "author": Henry_Miller, "category": Mindfulness},
    {"text": "There is no past or future for the enlightened. The past is remembered but not lived. The future is anticipated but not obsessed over. The present is what there is.", "author": Deepak_Chopra, "category": Mindfulness},
    {"text": "Hope is being able to see that there is light despite all of the darkness.", "author": Desmond_Tutu, "category": Hope},
    {"text": "Keep your face always toward the sunshine—and shadows will fall behind you.", "author": Walt_Whitman, "category": Hope},
    {"text": "There is some good in this world, and it's worth fighting for.", "author": J_R_R_Tolkien, "category": Hope},
    {"text": "In a time of destruction, create something.", "author": Maxine_Hong_Kingston, "category": Hope},
    {"text": "Once you choose hope, anything's possible.", "author": Christopher_Reeve, "category": Hope},
    {"text": "Hope is the heartbeat of the soul.", "author": Michelle_Horst, "category": Hope},
    {"text": "Hope itself is like a star- not to be seen in the sunshine of prosperity, and only to be discovered in the night of adversity.", "author": Charles_H_Spurgeon, "category": Hope},
    {"text": "Hope begins in the dark, the stubborn hope that if you just show up and try to do the right thing, the dawn will come. You wait and watch and work: you don't give up.", "author": Anne_Lamott, "category": Hope},
    {"text": "Do not spoil what you have by desiring what you have not; remember that what you now have was once among the things you only hoped for.", "author": Epicurus, "category": Hope},
    {"text": "You may not always have a comfortable life and you will not always be able to solve all of the world's problems at once but don't ever underestimate the importance you can have because history has shown us that courage can be contagious and hope can take on a life of its own.", "author": Michelle_Obama, "category": Hope},
    {"text": "Hope is like the sun, which, as we journey toward it, casts the shadow of our burden behind us.", "author": Samuel_Smiles, "category": Hope},
    {"text": "There is no medicine like hope, no incentive so great, and no tonic so powerful as expectation of something tomorrow.", "author": Orison_Swett_Marden, "category": Hope},
    {"text": "A friend is someone who knows all about you and still loves you.", "author": Elbert_Hubbard, "category": Friendship},
    {"text": "Friendship is the only cement that will ever hold the world together.", "author": Woodrow_Wilson, "category": Friendship},
    {"text": "True friendship comes when the silence between two people is comfortable.", "author": David_Tyson, "category": Friendship},
    {"text": "Friends are those rare people who ask how we are and then wait to hear the answer.", "author": Ed_Cunningham, "category": Friendship},
    {"text": "Friendship is always a sweet responsibility, never an opportunity.", "author": Khalil_Gibran, "category": Friendship},
    {"text": "A real friend is one who walks in when the rest of the world walks out.", "author": Walter_Winchell, "category": Friendship},
    {"text": "Friendship is the shadow of the evening, which increases with the setting sun of life.", "author": Jean_de_La_Fontaine, "category": Friendship},
    {"text": "A friend is what the heart needs all the time.", "author": Henry_Van_Dyke, "category": Friendship},
    {"text": "A friend is one that knows you as you are, understands where you have been, accepts what you have become, and still, gently allows you to grow.", "author": William_Shakespeare, "category": Friendship},
    {"text": "Friendship is the only thing in the world concerning the usefulness of which all mankind are agreed.", "author": Cicero, "category": Friendship},
    {"text": "Friendship marks a life even more deeply than love. Love risks degenerating into obsession, friendship is never anything but sharing.", "author": Elie_Wiesel, "category": Friendship},
    {"text": "A friend is someone who gives you total freedom to be yourself.", "author": Jim_Morrison, "category": Friendship},
    {"text": "Friendship consists in forgetting what one gives and remembering what one receives.", "author": Alexander_Dumas, "category": Friendship},
    {"text": "Friendship multiplies the good of life and divides the evil.", "author": Baltasar_Gracián, "category": Friendship},
    {"text": "Friendship is a plant of slow growth and must undergo and withstand the shocks of adversity before it is entitled to the appellation.", "author": George_Washington, "category": Friendship},
    {"text": "In the sweetness of friendship let there be laughter, for in the dew of little things the heart finds its morning and is refreshed.", "author": Khalil_Gibran, "category": Friendship},
    {"text": "The purpose of life is the expansion of happiness.", "author": Deepak_Chopra, "category": Courage},
    {"text": "Know the rules well, so you can break them effectively.", "author": Dalai_Lama, "category": Courage},
    {"text": "In matters of style, swim with the current; in matters of principle, stand like a rock.", "author": Johann_Wolfgang_von_Goethe, "category": Courage},
    {"text": "A man sees in the world what he carries in his heart.", "author": Johann_Wolfgang_von_Goethe, "category": Courage},
    {"text": "Manifest plainness, embrace simplicity, reduce selfishness, have few desires.", "author": Lao_Tzu, "category": Courage},
    {"text": "He who knows, does not speak. He who speaks, does not know.", "author": Lao_Tzu, "category": Courage},
    {"text": "Beauty is not in the face; beauty is a light in the heart.", "author": Khalil_Gibran, "category": Courage},
    {"text": "Rich people have small TVs and big libraries, and poor people have small libraries and big TVs.", "author": Zig_Ziglar, "category": Inspirational},
    {"text": "Don't let the silly little dramas of each day get you down. For you are here to do great things.", "author": Ralph_Marston, "category": Inspirational},
    {"text": "Death and life have their determined appointments; riches and honors depend upon heaven.", "author": Confucius, "category": Inspirational},
    {"text": "Patience expands your options. If you insist on immediate gratification, your choices are severely limited.", "author": Ralph_Marston, "category": Inspirational},
    {"text": "Some men see things as they are and ask why. Others dream things that never were and ask why not.", "author": George_Bernard_Shaw, "category": Inspirational},
    {"text": "Wise people, even though all laws were abolished, would still lead the same life.", "author": Aristophanes, "category": Inspirational},
    {"text": "The truth is rarely pure and never simple.", "author": Oscar_Wilde, "category": Inspirational},
    {"text": "Wealth is the product of man's capacity to think.", "author": Ayn_Rand, "category": Inspirational},
    {"text": "Weeds are flowers too, once you get to know them.", "author": A_A_Milne, "category": Inspirational},
    {"text": "Even when you think you have your life all mapped out, things happen that shape your destiny in ways you might never have imagined.", "author": Deepak_Chopra, "category": Inspirational},
    {"text": "You need a plan to build a house. To build a life, it is even more important to have a plan or goal.", "author": Zig_Ziglar, "category": Inspirational},
    {"text": "We run to win, not just to be in the race.", "author": Vince_Lombardi, "category": Inspirational},
    {"text": "If you want to achieve anything in this world, you have to get used to the idea that not everyone will like you.", "author": Simon_Sinek, "category": wisdom},
    {"text": "When you believe in a thing, believe in it all the way, implicitly and unquestionable.", "author": Walt_Disney, "category": wisdom},
    {"text": "Our greatest glory is not in never falling but in rising every time we fall.", "author": Confucius, "category": wisdom},
    {"text": "Hold yourself responsible for a higher standard than anybody else expects of you.", "author": Henry_Ward_Beecher, "category": wisdom},
    {"text": "Be kind, for everyone you meet is fighting a harder battle.", "author": Plato, "category": wisdom},
    {"text": "The whole problem with the world is the fools and fanatics are always so sure of themselves, and wiser people are full of doubts.", "author": George_Bernard_Shaw, "category": wisdom},
    {"text": "I learned that courage was not the absence of fear, but the triumph over it. The brave man is not he who does not feel afraid, but he who conquers that fear.", "author": Mandela, "category": wisdom},
    {"text": "Trust thyself: every heart vibrates to that iron string.", "author": Ralph_Waldo_Emerson, "category": wisdom},
    {"text": "When you realize you've made a mistake, take immediate steps to correct it.", "author": Dalai_Lama, "category": wisdom},
    {"text": "Sometimes letting things go is an act of far greater power than defending or hanging on.", "author": Eckhart_Tolle, "category": wisdom},
    {"text": "Go as far as you can see and you will see further.", "author": Zig_Ziglar, "category": wisdom},
    {"text": "The question isn't who is going to let me; it's who is going to stop me.", "author": Ayn_Rand, "category": wisdom},
    {"text": "Honor is the foundation of courage.", "author": Amelia_Earhart, "category": Courage},
    {"text": "One must be poor to know the luxury of giving.", "author": George_Eliot, "category": wisdom},
    {"text": "A creative man is motivated by the desire to achieve, not by the desire to beat others.", "author": Ayn_Rand, "category": wisdom},
    {"text": "Every great change is preceded by chaos.", "author": Deepak_Chopra, "category": wisdom},
    {"text": "We are what we repeatedly do. Excellence, then, is not an act, but a habit.", "author": Aristotle, "category": wisdom},
    {"text": "The quality, not the longevity, of one's life is what is important.", "author": Martin_Luther, "category": Motivational},
    {"text": "It doesn't matter how much you want. What really matters is how much you want it.", "author": Ralph_Marston, "category": Motivational},
    {"text": "Allow motion to equal emotion.", "author": Elbert_Hubbard, "category": Motivational},
    {"text": "To be alive - is Power.", "author": Emily_Dickinson, "category": Motivational},
    {"text": "Be - don't try to become", "author": Osho, "category": Motivational},
    {"text": "Never let the things you can't do stop you from doing what you can.", "author": Ronald_Reagan, "category": Motivational},
    {"text": "Rest when you're weary. Refresh and renew yourself, your body, your mind, your spirit. Then get back to work.", "author": Ralph_Marston, "category": Motivational},
    {"text": "Be as simple as you can be; you will be astonished to see how uncomplicated and happy your life can become.", "author": Paramahansa_Yogananda, "category": Motivational},
    {"text": "You are not the drop in the ocean, but the ocean in the drop.", "author": Deepak_Chopra, "category": Motivational},
    {"text": "If you aim at nothing, you will hit it every time.", "author": Zig_Ziglar, "category": love},
    {"text": "Success is stumbling from failure to failure with no loss of enthusiasm.", "author": Churchill, "category": Motivational},
    {"text": "Just do what must be done. This may not be happiness but it is greatness.", "author": George_Bernard_Shaw, "category": Inspirational},
    {"text": "If you love somebody, let them go, for if they return, they were always yours. If they don't, they never were.", "author": Khalil_Gibran, "category": love},
    {"text": "Remember that the best relationship is one in which your love for each other exceeds your need for each other.", "author": Dalai_Lama, "category": love},
    {"text": "To know even one life has breathed easier because you have lived. This is to have succeeded.", "author": Ralph_Waldo_Emerson, "category": Inspirational},
    {"text": "Decide whether or not the goal is worth the risks involved. If it is, stop worrying.", "author": Amelia_Earhart, "category": Motivational},
    {"text": "People don't realize that now is all there ever is; there is no past or future except as memory or anticipation in your mind.", "author": Eckhart_Tolle, "category": Courage},
    {"text": "Inspiration exists, but it has to find you working.", "author": Pablo_Picasso, "category": Inspirational},
    {"text": "We must learn to live together as brothers or perish together as fools.", "author": Martin_Luther, "category": love},
    {"text": "There are no secrets to success. It is the result of preparation, hard work, and learning from failure.", "author": Colin_Powell, "category": Inspirational},
    {"text": "The meaning of life is to find your gift. The purpose of life is to give it away.", "author": Pablo_Picasso, "category": wisdom},
    {"text": "When you make a choice, you change the future.", "author": Deepak_Chopra, "category": wisdom},
    {"text": "You find peace not by rearranging the circumstances of your life, but by realizing who you are at the deepest level.", "author": Eckhart_Tolle, "category": Inspirational},
    {"text": "Life is like riding a bicycle. To keep your balance you must keep moving.", "author": Einstein, "category": Creativity},
    {"text": "Every artist dips his brush in his own soul, and paints his own nature into his pictures.", "author": Henry_Ward_Beecher, "category": Creativity},
    {"text": "Sometimes your joy is the source of your smile, but sometimes your smile can be the source of your joy.", "author": Thich_Nhat_Hanh, "category": Creativity},
    {"text": "Get mad, then get over it.", "author": Colin_Powell, "category": Motivational},
    {"text": "Man should fear never beginning to live.", "author": Marcus_Aurelius, "category": Inspirational},
    {"text": "Trying to predict the future is like trying to drive down a country road at night with no lights while looking out the back window.", "author": Peter_Drucker, "category": wisdom},
    {"text": "There is no way to happiness - happiness is the way.", "author": Thich_Nhat_Hanh, "category": Happiness},
    {"text": "You play the hand you're dealt. I think the game's worthwhile.", "author": Christopher_Reeve, "category": Creativity},
    {"text": "The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty.", "author": Churchill, "category": Motivational},
    {"text": "I have never let my schooling interfere with my education.", "author": Mark_Twain, "category": Creativity},
    {"text": "Nothing is easier than fault finding.", "author": Og_Mandino, "category": wisdom},
    {"text": "Sometimes you put walls up not to keep people out, but to see who cares enough to break them down.", "author": Socrates, "category": Creativity},
    {"text": "The greatest discovery of all time is that a person can change their future by merely changing their attitude.", "author": Oprah, "category": Inspirational},
    {"text": "If anything is worth doing, do it with all your heart.", "author": Buddha, "category": Creativity},
    {"text": "he enemy is a very good teacher.", "author": Dalai_Lama, "category": Courage},
    {"text": "Everyone is a moon, and has a dark side which he never shows to anybody.", "author": Mark_Twain, "category": Creativity},
    {"text": "My actions are my only true belongings. I cannot escape the consequences of my actions. My actions are the ground upon which I stand.", "author": Thich_Nhat_Hanh, "category": Creativity},
    {"text": "Lack of direction, not lack of time, is the problem. We all have twenty-four hour days.", "author": Zig_Ziglar, "category": wisdom},
    {"text": "Memory is the scribe of the soul.", "author": Aristotle, "category": Leadership},
    {"text": "He who can no longer pause to wonder and stand rapt in awe, is as good as dead; his eyes are closed.", "author": Einstein, "category": Leadership},
    {"text": "What a liberation to realize that 'the voice in my head' is not who I am. Who am I then? The one who sees that.", "author": Eckhart_Tolle, "category": Leadership},
    {"text": "Every defeat, every heartbreak every loss, contains its own seed, its own lesson on how to improve your performance the next time.", "author": Og_Mandino, "category": Leadership},
    {"text": "Excellence is not a skill. It is an attitude.", "author": Ralph_Marston, "category": Leadership},
    {"text": "Try to be a rainbow in someone's cloud.", "author": Maya_Angelou, "category": Leadership},
    {"text": "The fear of death follows from the fear of life. A man who lives fully is prepared to die at any time.", "author": Mark_Twain, "category": life},
    {"text": "Whenever people agree with me I always feel I must be wrong.", "author": Oscar_Wilde, "category": Leadership},
    {"text": "One of the most difficult things is not to change society - but to change yourself.", "author": Mandela, "category": Inspirational},
    {"text": "The soul should always stand ajar, ready to welcome the ecstatic experience.", "author": Emily_Dickinson, "category": Friendship},
    {"text": "The person who never made a mistake never tried anything new.", "author": Einstein, "category": Motivational},
    {"text": "Not doing it is certainly the best way to not getting it.", "author": Wayne_Gretzky, "category": Friendship},
    {"text": "Go and do the things you can't. That is how you get to do them", "author": Pablo_Picasso, "category": Motivational},
    {"text": "Give more than you think you can, trusting that you are richer than you think.", "author": Jon_Kabat_Zinn, "category": Friendship},
    {"text": "I no doubt deserved my enemies, but I don't believe I deserved my friends.", "author": Walt_Whitman, "category": Friendship},
    {"text": "The friend is the man who knows all about you, and still likes you.", "author": Elbert_Hubbard, "category": Friendship},
    {"text": "Today will never happen again. Don't waste it with a false start or no start at all.", "author": Og_Mandino, "category": Friendship},
    {"text": "Dream big. Start small. But most of all, start.", "author": Simon_Sinek, "category": Friendship},
    {"text": "Attitude, not aptitude, determines altitude.", "author": Zig_Ziglar, "category": Friendship},
    {"text": "The way out is in.", "author": Thich_Nhat_Hanh, "category": wisdom},
    {"text": "Leadership is solving problems", "author": Colin_Powell, "category": Leadership},
    {"text": "Failure is the highway to success.", "author": Og_Mandino, "category": Motivational},
    {"text": "Don't let the behavior of others destroy your inner peace.", "author": Dalai_Lama, "category": Courage},
    {"text": "If I persist long enough I will win.", "author": Og_Mandino, "category": Dreams},
    {"text": "Don't be afraid to see what you see.", "author": Ronald_Reagan, "category": Dreams},
    {"text": "What you get by achieving your goals is not as important as what you become by achieving your goals.", "author": Henry_David_Thoreau, "category": Dreams},
    {"text": "The world doesn't owe you anything. It was here first.", "author": Mark_Twain, "category": Gratitude},
    {"text": "If you want to feel happy, do something for yourself. If you want to feel fulfilled, do something for someone else.", "author": Simon_Sinek, "category": Mindfulness},
    {"text": "A man that flies from his fear may find that he has only taken a short cut to meet it.", "author": J_R_R_Tolkien, "category": wisdom},
    {"text": "Intelligence, imagination, and knowledge are essential resources, but only effectiveness converts them into results.", "author": Peter_Drucker, "category": Motivational},
    {"text": "There is no right or wrong, only a series of possibilities that shift with each thought, feeling, and action that you experience.", "author": Deepak_Chopra, "category": Adventure},
    {"text": "Forever is composed of now's.", "author": Emily_Dickinson, "category": Inspirational},
    {"text": "Follow your instincts. That is where true wisdom manifests itself.", "author": Oprah, "category": wisdom},
    {"text": "Failure will never overtake me if my determination to succeed is strong enough.", "author": Og_Mandino, "category": Adventure},
    {"text": "Rudeness is the weak man's imitation of strength.", "author": Eric_Hoffer, "category": Courage},
    {"text": "As one grows weaker one is less susceptible to suffering. There is less hurt because there is less to hurt.", "author": Jack_London, "category": wisdom},
    {"text": "People become attached to their burdens sometimes more than the burdens are attached to them.", "author": George_Bernard_Shaw, "category": Adventure},
    {"text": "You will face many defeats in life, but never let yourself be defeated.", "author": Maya_Angelou, "category": Inspirational},
    {"text": "Repetition does not transform a lie into a truth.", "author": Roosevelt, "category": wisdom},
    {"text": "Life is not always a matter of holding good cards, but sometimes, playing a poor hand well.", "author": Jack_London, "category": Adventure},
    {"text": "You can have it all. You just can't have it all at once.", "author": Oprah, "category": Adventure},
    {"text": "There are more quarrels smothered by just shutting your mouth, and holding it shut, than by all the wisdom in the world.", "author": Henry_Ward_Beecher, "category": wisdom},
    {"text": "The positive thinker sees the invisible, feels the intangible, and achieves the impossible.", "author": Churchill, "category": Adventure},
    {"text": "It is during our darkest moments that we must focus to see the light.", "author": Aristotle, "category": life},
    {"text": "What people need and what they want may be very different.", "author": Elbert_Hubbard, "category": life},
    {"text": "Expect the best of yourself, and then do what is necessary to make it a reality.", "author": Ralph_Marston, "category": life},
    {"text": "The power of man has grown in every sphere, except over himself.", "author": Churchill, "category": wisdom},
    {"text": "Winners never quit and quitters never win.", "author": Vince_Lombardi, "category": life},
    {"text": "You can avoid reality, but you cannot avoid the consequences of avoiding reality.", "author": Ayn_Rand, "category": Perseverance},
    {"text": "Life is either a daring adventure, or it is nothing.", "author": Helen_Keller, "category": Adventure},
    {"text": "There are no accidents... there is only some purpose that we haven't yet understood.", "author": Deepak_Chopra, "category": Perseverance},
    {"text": "I do not seek. I find.", "author": Pablo_Picasso, "category": Perseverance},
    {"text": "Success is the child of drudgery and perseverance. It cannot be coaxed or bribed; pay the price and it is yours.", "author": Orison_Swett_Marden, "category": Perseverance},
    {"text": "The harder the conflict, the greater the triumph.", "author": George_Washington, "category": Perseverance},
    {"text": "Work out your own salvation. Do not depend on others.", "author": Buddha, "category": Perseverance},
    {"text": "Simplicity is the glory of expression.", "author": Walt_Whitman, "category": Perseverance},
    {"text": "It is better to offer no excuse than a bad one.", "author": George_Washington, "category": Perseverance},
    {"text": "You never know when a moment and a few sincere words can have an impact on a life.", "author": Zig_Ziglar, "category": Hope},
    {"text": "Goodness is the only investment that never fails.", "author": Henry_David_Thoreau, "category": Kindness},
    {"text": "Give me six hours to chop down a tree and I will spend the first four sharpening the axe.", "author": Abraham_Lincoln, "category": Inspirational},
    {"text": "A man is but a product of his thoughts. What he thinks he becomes.", "author": Mahatma_Gandhi, "category": Hope},
    {"text": "Live and act within the limit of your knowledge and keep expanding it to the limit of your life.", "author": Ayn_Rand, "category": Hope},
    {"text": "Others can stop you temporarily - you are the only one who can do it permanently.", "author": Zig_Ziglar, "category": Motivational},
    {"text": "Alone we can do so little; together we can do so much.", "author": Helen_Keller, "category": Inspirational},
    {"text": "Loving thoughts and actions are clearly beneficial for our physical and mental health.", "author": Dalai_Lama, "category": Mindfulness},
    {"text": "Perseverance and spirit have done wonders in all ages.", "author": George_Washington, "category": Perseverance},
    {"text": "Pleasure is always derived from something outside you, whereas joy arises from within.", "author": Eckhart_Tolle, "category": wisdom},
    {"text": "Love is merely the name for the desire and pursuit of the whole.", "author": Aristophanes, "category": love},
    {"text": "Think of yourself as dead. you have lived your life. Now, take what's left, and live it properly.", "author": Marcus_Aurelius, "category": life},
    {"text": "A mistake is only an error, it becomes a mistake when you fail to correct it.", "author": John_Lennon, "category": Inspirational},
    {"text": "When you are able to employ your will always for constructive purposes, you become the controller of your destiny.", "author": Paramahansa_Yogananda, "category": Motivational},
    {"text": "The greatest mistake you can make in life is to be continually fearing you will make one.", "author": Elbert_Hubbard, "category": Hope},
    {"text": "I defeat my enemies when I make them my friends.", "author": Dalai_Lama, "category": Friendship},
    {"text": "What we dwell on is who we become.", "author": Oprah, "category": Hope},
    {"text": "We have more possibilities available in each moment than we realize.", "author": Thich_Nhat_Hanh, "category": Perseverance},
]

for quote_info in quotes_data:
    new_quote = Quote(text=quote_info["text"], author=quote_info["author"], category=quote_info["category"])
    storage.new(new_quote)


storage.save()


all_quotes = storage.all(Quote)
for quote_key, quote_obj in all_quotes.items():
    print(f"{quote_obj.author.name}: '{quote_obj.text}' in category '{quote_obj.category.name}'")
