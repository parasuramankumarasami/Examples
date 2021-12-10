import json, base64, httplib2
from json import dumps
from datetime import datetime
import time
testuc_login_url = 'https://auth.alpha.shoretel.com/api/1.0/login'

h = httplib2.Http(disable_ssl_certificate_validation=True)
gettoken = {"identity":"pkumarasami@alpha.shoretel.com", "password": base64.b64encode(b'Abc123!!'), "locatorApiVersion":"1.0"}

resp, content = h.request(
        uri=testuc_login_url,
        method='POST',
        headers={'Content-Type': 'application/json'},
        body=dumps(gettoken)
)
print(resp)
print(content)

mydict = json.loads(content)

channel_url = mydict.get("serviceLocatorUrl")
channel_url = channel_url+"/services/channel?ver=1.0"
channelres, channelcontent = h.request(channel_url, method='GET', body='', headers={'Content-Type': 'application/json', 'Authorization':'Bearer '+mydict.get("token")})

print(channelres)
print(channelcontent)

channeldic = json.loads(channelcontent)

teamworkurl = channeldic.get("url")

createwsurl = teamworkurl+"/workspaces"

for x in range(1, 2):
    wsname = datetime.now()
    createwswithmembody = '''{
    "title":"'''+str(wsname)+'''",
    "description":"automation sanity Test",
    "searchable":"true",
    "access_model":"local",
    "default_affiliation":"moderator"}'''
    
    createwsres, createwscontent = h.request(createwsurl, 
       method='POST',
       body=createwswithmembody,
       headers={'Content-Type': 'application/json','Authorization':'Bearer '+mydict.get("token")})
    
    print(createwsres)
    print(createwscontent)
    channeldic = json.loads(createwscontent)

    jid = channeldic.get("jid")
    print(jid)
    postmsg = teamworkurl+"/"+jid+"/content/posts"
    msg = '''{"content":"Hi, Parasu"}'''
    createwsres, createwscontent = h.request(postmsg, 
       method='POST',
       body=msg,
       headers={'Content-Type': 'application/json','Authorization':'Bearer '+mydict.get("token")})
    
    print(createwsres)
    print(createwscontent)
    
    postmsgcontent = '''Mitel Teamwork provides collaborative web, desktop, and mobile applications for users with a supported phone profile (Essentials, Premier, or Elite) in a MiCloud Connect phone system. '''
    postmsg = teamworkurl+"/"+jid+"/content/posts"
    msg = '''{"content":"'''+postmsgcontent+'''"}'''
    createwsres, createwscontent = h.request(postmsg, 
       method='POST',
       body=msg,
       headers={'Content-Type': 'application/json','Authorization':'Bearer '+mydict.get("token")})
    time.sleep(3)
    print(createwsres)
    print(createwscontent)
    postmsgcontent = '''Use the instructions below to access the Teamwork web and desktop applications. You need to accept the Mitel software license agreement to use these applications. When you close the Teamwork web or desktop application and then open or log into the application again, '''
    postmsg = teamworkurl+"/"+jid+"/content/posts"
    msg = '''{"content":"'''+postmsgcontent+'''"}'''
    createwsres, createwscontent = h.request(postmsg, 
       method='POST',
       body=msg,
       headers={'Content-Type': 'application/json','Authorization':'Bearer '+mydict.get("token")})
    time.sleep(3)
    print(createwsres)
    print(createwscontent)
    postmsgcontent = '''The main purpose of Mitel Teamwork is to provide workers with a virtual gathering place known as a workspace. You can create a workspace for any size team, project, group, or event. Every message, task, and file added to a workspace is displayed so all workspace members can easily find all relevant information.'''
    postmsg = teamworkurl+"/"+jid+"/content/posts"
    msg = '''{"content":"'''+postmsgcontent+'''"}'''
    createwsres, createwscontent = h.request(postmsg, 
       method='POST',
       body=msg,
       headers={'Content-Type': 'application/json','Authorization':'Bearer '+mydict.get("token")})
    time.sleep(3)
    print(createwsres)
    print(createwscontent)
    postmsgcontent = '''Workspace messages are listed by date in chronological order with the most recent message displayed at the bottom of a workspace and the oldest message displayed at the top. To see all older messages, scroll upwards until you see the words You have reached the top When viewing a workspace,'''
    postmsg = teamworkurl+"/"+jid+"/content/posts"
    msg = '''{"content":"'''+postmsgcontent+'''"}'''
    createwsres, createwscontent = h.request(postmsg, 
       method='POST',
       body=msg,
       headers={'Content-Type': 'application/json','Authorization':'Bearer '+mydict.get("token")})
    time.sleep(3)
    print(createwsres)
    print(createwscontent)
    postmsgcontent = '''To post a new message that can be read by all members of a workspace, select the desired workspace, type a message, and press Enter. Optionally, you can add an emoji to your message by scrolling through the menu that opens via the smiley face icon on the right side of the message input area.'''
    postmsg = teamworkurl+"/"+jid+"/content/posts"
    msg = '''{"content":"'''+postmsgcontent+'''"}'''
    createwsres, createwscontent = h.request(postmsg, 
       method='POST',
       body=msg,
       headers={'Content-Type': 'application/json','Authorization':'Bearer '+mydict.get("token")})
    time.sleep(3)
    print(createwsres)
    print(createwscontent)
    postmsgcontent = '''When posting a message, you can generate notifications to specific people by including @mentions or you can notify all members of the workspace by including @all. To notify someone with an @mention, type @ followed by the first few letters of the desired member's name and click the desired name in the pop-up menu that appears (or use the arrow keys to highlight the desired name in the menu and press Enter). To notify all workspace members, type @all and click @all in the pop-up menu that appears (or press Enter when @all displays in the menu).'''
    postmsg = teamworkurl+"/"+jid+"/content/posts"
    msg = '''{"content":"'''+postmsgcontent+'''"}'''
    createwsres, createwscontent = h.request(postmsg, 
       method='POST',
       body=msg,
       headers={'Content-Type': 'application/json','Authorization':'Bearer '+mydict.get("token")})
    time.sleep(3)
    print(createwsres)
    print(createwscontent)
    postmsgcontent = '''To edit a workspace message that you posted previously, hover over the message and click the pencil Edit Workspace Message Icon icon in the menu that appears (on the right side of the message). In the Edit Message dialog that opens, make changes to the message, add any number of emoticons by clicking the smiley face icon on the right side of the dialog, and click Save. Editing a message enables you to change a reply, fix a typo, add an @mention, etc. You can edit a message as often as needed. '''
    postmsg = teamworkurl+"/"+jid+"/content/posts"
    msg = '''{"content":"'''+postmsgcontent+'''"}'''
    createwsres, createwscontent = h.request(postmsg, 
       method='POST',
       body=msg,
       headers={'Content-Type': 'application/json','Authorization':'Bearer '+mydict.get("token")})
    time.sleep(3)
    print(createwsres)
    print(createwscontent)
    postmsgcontent = '''To reply to a message, hover over the message, click the Reply Reply icon in the menu that appears (on the right side of the message), type your reply, and press Enter. The original message is repeated with your reply so all workspace members can see the context of the reply. Optionally, you can add an emoji to your reply by scrolling through the menu that opens via the smiley face icon on the right side of the message input area.'''
    postmsg = teamworkurl+"/"+jid+"/content/posts"
    msg = '''{"content":"'''+postmsgcontent+'''"}'''
    createwsres, createwscontent = h.request(postmsg, 
       method='POST',
       body=msg,
       headers={'Content-Type': 'application/json','Authorization':'Bearer '+mydict.get("token")})
    time.sleep(3)
    print(createwsres)
    print(createwscontent)
    postmsgcontent = '''To respond to a message by posting a reaction, hover over the message, select the smiley face icon in the menu that appears (on the right side of the message), and select the desired reaction emoji. All reactions to a message are displayed below the message summarized by emoji type with counts for each type. When you click the reaction summary area displaying the emojis, a list displays all workspace members and their reactions.'''
    postmsg = teamworkurl+"/"+jid+"/content/posts"
    msg = '''{"content":"'''+postmsgcontent+'''"}'''
    createwsres, createwscontent = h.request(postmsg, 
       method='POST',
       body=msg,
       headers={'Content-Type': 'application/json','Authorization':'Bearer '+mydict.get("token")})
    time.sleep(3)
    print(createwsres)
    print(createwscontent)
    postmsgcontent = '''To delete a message that you posted previously, hover over the message, click the three dots dot-dot-dot icon in the menu that appears (on the right side of the message), and select the Delete Message option.'''
    postmsg = teamworkurl+"/"+jid+"/content/posts"
    msg = '''{"content":"'''+postmsgcontent+'''"}'''
    createwsres, createwscontent = h.request(postmsg, 
       method='POST',
       body=msg,
       headers={'Content-Type': 'application/json','Authorization':'Bearer '+mydict.get("token")})
    time.sleep(3)
    print(createwsres)
    print(createwscontent)
    postmsgcontent = '''When you have one or more unread workspace messages or notifications, an orange Workspace Message Indicator dot is displayed next to the workspace name. Teamwork also provides other types of indicators to let you know there are one or more new messages or notifications that you have not yet viewed. To learn about the types of activities that generate notifications and where the notifications are displayed, see the Notifications section of this article.'''
    postmsg = teamworkurl+"/"+jid+"/content/posts"
    msg = '''{"content":"'''+postmsgcontent+'''"}'''
    createwsres, createwscontent = h.request(postmsg, 
       method='POST',
       body=msg,
       headers={'Content-Type': 'application/json','Authorization':'Bearer '+mydict.get("token")})
    time.sleep(3)
    print(createwsres)
    print(createwscontent)
    postmsgcontent = '''The DIRECT MESSAGES list on the left side of Teamwork provides access to your direct and SMS messages. The most recent messages are displayed at the top of the list. Personal 1:1 messages are listed by the first and last name of the contact and group messages are listed by the first names of up to three contacts. To view all contacts for a group message, hover over the group names in the DIRECT '''
    postmsg = teamworkurl+"/"+jid+"/content/posts"
    msg = '''{"content":"'''+postmsgcontent+'''"}'''
    createwsres, createwscontent = h.request(postmsg, 
       method='POST',
       body=msg,
       headers={'Content-Type': 'application/json','Authorization':'Bearer '+mydict.get("token")})
    time.sleep(3)
    print(createwsres)
    print(createwscontent)
    postmsgcontent = '''To view all tasks for a workspace, select the desired workspace and click the Tasks Tasks icon in the top-right corner of the workspace page. In the Tasks panel that opens, click To Do (the default view) to view pending tasks or click Completed to view completed tasks. To view only tasks assigned to you, click the My Tasks checkbox. To filter your view of To Do or Completed tasks, click the Filter Tasks icon and select the Overdue or High Priority option (Overdue applies only to the To Do tasks). '''
    postmsg = teamworkurl+"/"+jid+"/content/posts"
    msg = '''{"content":"'''+postmsgcontent+'''"}'''
    createwsres, createwscontent = h.request(postmsg, 
       method='POST',
       body=msg,
       headers={'Content-Type': 'application/json','Authorization':'Bearer '+mydict.get("token")})
    time.sleep(3)
    print(createwsres)
    print(createwscontent)
    postmsgcontent = '''When you are typing text in the "Type a message here" area, your name followed by "is typing" appears on the message screen for each of the contacts who are receiving your message. When a contact is typing text to send you a message, you will see that person's name followed by "is typing" on the message screen. If you are chatting with multiple contacts who are typing simultaneously, the typing indicator shows the first name of up to three contacts.'''
    postmsg = teamworkurl+"/"+jid+"/content/posts"
    msg = '''{"content":"'''+postmsgcontent+'''"}'''
    createwsres, createwscontent = h.request(postmsg, 
       method='POST',
       body=msg,
       headers={'Content-Type': 'application/json','Authorization':'Bearer '+mydict.get("token")})
    time.sleep(3)
    print(createwsres)
    print(createwscontent)
