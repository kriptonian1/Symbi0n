import random

class Utils():

    meme_links = ['https://memes.blademaker.tv/api?lang=en','https://memes.blademaker.tv/api/dankmemes','https://memes.blademaker.tv/api/funny','https://memes.blademaker.tv/api/madlad','https://memes.blademaker.tv/api/ComedyCemetery','https://memes.blademaker.tv/api/comedyheaven','https://memes.blademaker.tv/api/technicallythetruth','https://memes.blademaker.tv/api/softwaregore','https://memes.blademaker.tv/api/me_irl','https://memes.blademaker.tv/api/TIHI','https://memes.blademaker.tv/api/facepalm','https://memes.blademaker.tv/api/meme','https://memes.blademaker.tv/api/comics','https://memes.blademaker.tv/api/wholesomememes','https://memes.blademaker.tv/api/goodanimemes']
    nsfw_links = ['https://memes.blademaker.tv/api/nswf','https://memes.blademaker.tv/api/MildlyVandalised','https://memes.blademaker.tv/api/SuddenlyGay','https://memes.blademaker.tv/api/suddenlysexoffender','https://memes.blademaker.tv/api/cursedcomments','https://memes.blademaker.tv/api/MurderedByWords','https://memes.blademaker.tv/api/rareinsults','https://memes.blademaker.tv/api/NoahGetTheBoat','https://memes.blademaker.tv/api/NSFWFunny','https://memes.blademaker.tv/api/shitposting','https://memes.blademaker.tv/api/NoRules','https://memes.blademaker.tv/api/Cursed_Images','https://memes.blademaker.tv/api/PornhubComments','https://memes.blademaker.tv/api/fakehistoryporn','https://memes.blademaker.tv/api/4chan','https://memes.blademaker.tv/api/okbuddyretard']
    porn_links = ['https://memes.blademaker.tv/api/onlyfansgirls101','https://memes.blademaker.tv/api/Nude_Selfie','https://memes.blademaker.tv/api/gonewild','https://memes.blademaker.tv/api/RealGirls','https://memes.blademaker.tv/api/BustyPetite','https://memes.blademaker.tv/api/LegalTeens','https://memes.blademaker.tv/api/PetiteGoneWild','https://memes.blademaker.tv/api/adorableporn','https://memes.blademaker.tv/api/AsiansGoneWild','https://memes.blademaker.tv/api/collegesluts','https://memes.blademaker.tv/api/Amateur','https://memes.blademaker.tv/api/OnOff','https://memes.blademaker.tv/api/HappyEmbarrassedGirls']
    hentai_links = ['https://memes.blademaker.tv/api/rule34/','https://memes.blademaker.tv/api/hentai/']
    truth_questions = ["What's the biggest lie you've told to somebody in this room?","What question would you least like to be asked?","Have you ever gone a day without underwear?","What is one thing about yourself you try to keep hidden?","Have you ever done something against the law?","When was the last time you peed in a swimming pool?","What's something you secretly like but are embarrassed by?","What's something about yourself that would scare other people if they knew?","Do you have a diary?","Have you ever watched an *adult film*?","Who is your favourite person in this room?","Who are your two least favourite people in this room?","When was the last time you wet your pants?","Have you ever pooped in your pants?","If you were the opposite sex for an hour, what would you do?","List all the things in your room that you have made some attempt to hide.","What's the worst thing you've ever done to your parents?","What's the most embarrassing thing you've been to the doctor for?","What's the most expensive thing you've broken?","What's the worst thing you've ever done to your siblings?","If you could be invisible for 2 hours, what would you do?","What's the most embarrassing song you like?","What's the most embarrassing TV show you like?","What's the most embarrassing website you like?","What's the most embarrassing movie you like?","What Was Your First Kiss Like?","What Is Your Least Favorite Thing About Your Best Friend?","Have You Ever Committed A Crime? If So, What Was It?","Have You Ever Cried From Watching A TV Show Or A Movie?"," What Do You Do When You Are Alone And No One Is Watching You?","What Is One Thing That You Have Always Wanted To Do But Have Not Gotten Around To It Yet?",'Who is the sexiest person in this room?','Who is your current crush?']
    dare_questions = ["Do a *show and tell* with the ENTIRE contents of your purse","Pick your nose and eat it in front of the group.",'''Text five people in your phone contacts list with the message "I'm awesome!"''',"Make a rap song about (insert topic) and perform it to the group.","Put an ice cube down your back.","Imitate another player and have everyone guess who you are.","Do an imitation of Tarzan.","Pick One Person In The Group, What Is Some Honest Relationship Advice You Would Give Them?","Tell Us About Your Five Bad Habits.","Do 50 sit ups.","Send a love letter to someone on Whatsapp(except the person playing the game).",'Send someone a message that says, “I know what you did last summer.”',"Say the alphabet backwards.","Call someone on your phone and talk to them for 5 minutes without telling them that you are playing Truth or Dare.","Prank call someone and pretend she/he is your girlfriend/boyfriend and propose to him/her.","Try to do a stand up comedy in front of the other players.","Show your whole browsing history to the players in the room.","Propose to the person under you in voice channel","Prank call someone and make them believe that they have won the lottery.","Prank call someone and tell them that you are horny.","Try to touch your nose with your tongue.","Call your closest friend and invite him/her for a threesome.","Make out with your hand.","Post an old selfie on your Instagram story.","Do 30 situps."]
    four_corner_die = [1,2,3,4]
    six_corner_die = [1,2,3,4,5,6]
    eight_corner_die = [1,2,3,4,5,6,7,8]
    ten_corner_die = [1,2,3,4,5,6,7,8,9,10]
    twelve_corner_die = [1,2,3,4,5,6,7,8,9,10,11,12]
    twenty_corner_die = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    def get_meme_link(self):
        return random.choice(self.meme_links)

    def get_nsfw_link(self):
        return random.choice(self.nsfw_links)

    def get_porn_link(self):
        return random.choice(self.porn_links)

    def get_hentai_link(self):
        return random.choice(self.hentai_links)

    def get_truth_question(self):
        return random.choice(self.truth_questions)

    def get_dare_question(self):
        return random.choice(self.dare_questions)

    def get_die(self, die_face):
	    if die_face == '4':
	    	return random.choice(self.four_corner_die)
	    elif die_face == '6':
	    	return random.choice(self.six_corner_die)
	    elif die_face == '8':
	    	return random.choice(self.eight_corner_die)
	    elif die_face == '12':
	    	return random.choice(self.twelve_corner_die)
	    elif die_face == '20':
	    	return random.choice(self.twenty_corner_die)
	    else:
	    	if die_face%2 == 0:
	    		return random.randint(1,die_face)
	    	else:
	    		return "This is not a vaild die!"

    def get_merlin(self, question):
	    import http.client
	    import json
	    import urllib.parse
	    conn = http.client.HTTPSConnection("8ball.delegator.com")
	    question = urllib.parse.quote(question)
	    conn.request('GET', '/magic/JSON/' + question)
	    response = conn.getresponse()
	    ans=(json.loads(response.read()))
	    return (ans['magic']['answer'])