"""
Plugin for monitoring new adds to HOs and alerting if users were not added by an admin or mod.
Add mods to the config.json file either globally or on an individual HO basis.
Add a "watch_new_adds": true  parameter to individual HOs in the config.json file.

Author: @Riptides
"""

import hangups

import plugins


def _initialise(bot):
    plugins.register_handler(_watch_new_adds, type="membership")
    plugins.register_admin_command(["addmod", "delmod"])


def _watch_new_adds(bot, event, command):
    # Check if watching for new adds is enabled
    if not bot.get_config_suboption(event.conv_id, 'watch_new_adds'):
        return

    # Generate list of added or removed users
    event_users = [event.conv.get_user(user_id) for user_id
                   in event.conv_event.participant_ids]
    names = ', '.join([user.full_name for user in event_users])

    # JOIN
    if event.conv_event.type_ == hangups.MembershipChangeType.JOIN:
        # Check if the user who added people is a mod or admin
        admins_list = bot.get_config_suboption(event.conv_id, 'admins')
        if event.user_id.chat_id in admins_list:
            return

        mods_list = bot.get_config_suboption(event.conv_id, 'mods')
        try:
            if event.user_id.chat_id in mods_list:
                return
        except TypeError:
            # The mods are likely not configured. Continuing...
            pass

## Putting welcome note for the L3+ and Resistance LK hangouts when a new agent 
## is added.

        ho_name = bot.get_config_suboption(event.conv_id, 'ho_name')
        L3_plus1 = 'L3_plus1'
        L3_plus2 = 'L3_plus2'
        res_lk1 = 'res_lk1'
        res_lk2 = 'res_lk2'
        welcome1 = 'welcome1'
        welcome2 = 'welcome2'
        if ho_name == L3_plus1 or ho_name == L3_plus2:
            html = "<b>---  🙋 Hello {} ---</b><br /><br />".format(names)
            html += "<i> <b> Welcome to the L3+ Clearance Resistance LK hangout  </b> </i>"
            html += "This is an official communication channel of "
            html += "Ingress Resistance - Sri Lanka agents who have cleared Level 3."
            html += "You have been added here because you have worked hard to reach L3 (or higher) and proved that you are a good, genuine and a serious Resistance player."
            html += "Since this a fun filled channel with chatting, bantering and strategy talk, simply turn the notifications <b> Off </b>  if it\'s disturbing you. However we\'d like you to check this hangout now and then to learn what\'s happening. Specially if you are playing or passing through a new area, give a heads up for others.<br />"
            html += "There are couple of rules though. <br /><br />"
            html += "1. Since the in-game COMM can be spied-on, this is our secure channel to talk. So please keep this our little secret.Don\'t discuss this hangout with anyone who\'s not in it. Specially not with anyone from the opposing faction (fondly called Frogs). Don\'t talk about details discussed here even with Resistance agents who aren\'t here, not even in our G+ community. <br /> <br />"
            html += "2. If you\'d like to add someone else to this hangout, you should get consent from L7 & L8 agents who are here. Anyone below L3 won\'t be added. Anyone whose identity isn\'t vouched by someone here (including you) won\'t be added."
            html += "Once again, let us stress the importance of your effort to keep this hangout a secret, specially if you work or live with Frogs. When you get involved with Operations/Missions and when you get to higher levels you will naturally adapt. <br /> <br />"
            html += "- Please join our Google+ Community at:https://plus.google.com/u/0/communities/103148601223092157948 <br />"
            html += "- Follow us on twitter @lkresistance (https://twitter.com/LKResistance) <br />"
            html += "- Follow us on Facebook:https://www.facebook.com/SLKResistance <br />"
            html += "So have fun. Make friends, and most of all, Happy Ingressing! <br /> <br /><b>{}</b> Please read the above message and confirm............".format(names)
            bot.send_html_to_conversation(event.conv, html)
        
        elif ho_name == res_lk1 or ho_name == res_lk2:
            html2 = "Dear <b>{}</b> ,<br /><br />".format(names)
            html2 += "Welcome to the innermost circle of the Sri Lankan Resistance, The Resistance LK group. This is as far as you can go. This is the only hangout that existed a long time ago when there were only few players. When the resistance started to grow stronger, we created the L3+ Clearance hangout which you were already in. This is the main group that contains agents who are L7 or higher and the group that is used to discuss the most secretive operations. <br /> <br />"

            html2 += "Hope you didn’t mind that we haven’t mentioned this group to you or added you to it earlier. The <b>L3 plus clearance</b> is used for the lower level agents and we don’t mention this group there. Once you reach L7, we add you here. <br /> <br />"

            html2 += "Now that you are L7 we have added you. Congratulations in making it to the most secretive group in Sri Lanka <br /> <br />"

            html2 += "We do the usual here, we chat about strategy and ops but we talk nonsense more than anything. As usual, it can get annoying with all the alerts, so configure the notifications to suite you if it’s disturbing you. <br /> <br />"

            html2 += "The same rules as L3+ applies here, firstly, is that you don’t talk about the Resistance LK or about what’s discussed here with anyone outside of it (even within the members of the L3+ Clearance). This you already knew with the other group <br /> <br />"

            html2 += "Secondly, anyone less than L7 cannot be added to this group and to add anyone you need the consent of the majority agents in here. <br /> <br />"
            html2 += "So, have fun, and all the best to L8 and Beyond! And as usual happy ingressing!"
            bot.send_html_to_conversation(event.conv, html2)
        
        elif ho_name == welcome1 or ho_name == welcome2:    
                        
            html3 = "<b> 🙋Welcome to the Resistance LK </b><br />"
            html3 += "Dear <b>{}</b> ,<br /><br />".format(names)
            html3 += "This is an official communication  channel of Ingress Resistance - Sri Lanka agents. You took the right decision by selecting Resistance to fight for protect humanity. You need to  work hard to be a good, genuine and a serious Resistance agent. There is a war... Between frogs and us. Your country need you. humanity need you...<br /><br />"

            html3 += "Please feel free to ask questions and be familiar with the community. We are here to help you. "

            html3 += "There are couple of rules though.<br /><br />"

            html3 += "1. Since the in-game COMM can be spied-on, this is our secure channel to talk. So please keep this our little secret. Don't discuss this hangout with anyone who's not in it. Specially not with anyone from the opposing faction (fondly called Frogs). Don't talk about details discussed here even with Resistance agents who aren't here, not even in our G+ community.<br /><br />"

            html3 += "2. If you'd like to add someone else to this, you should get consent from L7+ agents who are here and provide the email address of the agent so we can send an invite.<br /><br />"

            html3 += "Once again, let us stress the importance of your effort to keep this hangout a secret, specially if you work or live with 🐸 Frogs. When you get involved with Operations/Missions and when you get to higher levels you will naturally adapt.<br /><br />"
            html3 += "You may join the other channels except the one you automatically got joined to get more information.<br /><br />"

            html3 += "- Please join our Google+ Community at:https://plus.google.com/u/0/communities/103148601223092157948 <br /><br />"
            html3 += "- Follow us on twitter @lkresistance (https://twitter.com/LKResistance)<br /><br />"
            html3 += "- Follow us on Facebook:https://www.facebook.com/SLKResistance <br /><br />"

            html3 += "So have fun. Make friends, and most of all, Happy Ingressing "

            html3 += ".......... Please read above message and confirm it."
            bot.send_html_to_conversation(event.conv, html3)

def addmod(bot, event, *args):
    mod_ids = list(args)
    if(bot.get_config_suboption(event.conv_id, 'mods') != None):
        for mod in bot.get_config_suboption(event.conv_id, 'mods'):
            mod_ids.append(mod)
        bot.config.set_by_path(["mods"], mod_ids)
        bot.config.save()
        html_message = _("<i>Moderators updated: {} added</i>")
        bot.send_message_parsed(event.conv, html_message.format(args[0]))
    else:
        bot.config.set_by_path(["mods"], mod_ids)
        bot.config.save()
        html_message = _("<i>Moderators updated: {} added</i>")
        bot.send_message_parsed(event.conv, html_message.format(args[0]))

def delmod(bot, event, *args):
    if not bot.get_config_option('mods'):
        return
    
    mods = bot.get_config_option('mods')
    mods_new = []
    for mod in mods:
        if args[0] != mod:
            mods_new.append(mod)
    
    bot.config.set_by_path(["mods"], mods_new)
    bot.config.save()
    html_message = _("<i>Moderators updated: {} removed</i>")
    bot.send_message_parsed(event.conv, html_message.format(args[0]))
