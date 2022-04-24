import lightbulb
import hikari
import config

from lightbulb.ext import tasks

# START UP
# .\env\Scripts\activate
# py bot.py

bot = lightbulb.BotApp(
    token=config.bot_token,
    default_enabled_guilds=(config.test_guild_id),
    intents=(hikari.Intents.GUILD_MEMBERS |
             hikari.Intents.GUILD_MESSAGE_REACTIONS)
)

# Database
file = open("database.txt", "r")
users = []
for user in file:
    users.append(user.strip())

for i in range(len(users)):
    users[i] = users[i].split("  ")

# print(users)
# Load Extenstions (Commands)
bot.load_extensions("extensions.roles")
bot.load_extensions("extensions.mul")
bot.load_extensions("extensions.add")


@bot.listen(hikari.StartedEvent)
async def bot_started(event: hikari.StartingEvent) -> None:
    print('Bot has started!')


@bot.listen(hikari.StoppingEvent)
async def bot_stopping(event: hikari.StoppingEvent) -> None:
    file.close()
    newFile = open("database.txt", "w")
    for user in users:
        newFile.write(str(user[0]) + "  " +
                      str(user[1]) + "  " + str(user[2]) + "\n")
    newFile.close()


@bot.listen(hikari.MemberCreateEvent)  # New user joined server
async def new_member(event: hikari.MemberCreateEvent) -> None:
    user_id = str(event.member.id)
    users.append([user_id, "1", "0"])
    # print(users)


@bot.listen(hikari.GuildReactionAddEvent)
async def reaction_add(event: hikari.GuildReactionAddEvent) -> None:
    emoji_name = event.emoji_name
    channel_id = event.channel_id
    channel = await bot.rest.fetch_channel(channel_id)
    message_id = event.message_id
    message = await bot.rest.fetch_message(channel_id, message_id)
    author = str(message.author.id)
    if emoji_name == "retweet":
        for user in users:
            if str(user[0]) == author:
                user[2] = int(user[2])+1
                if (int(user[2]) >= 0 and int(user[2]) < 1 and int(user[1]) != 1):
                    user[1] = "1"
                    content = (message.author.mention +
                               " just hit level " + str(user[1]) + "!")
                    await bot.rest.create_message(channel, content)
                    break
                elif (int(user[2]) >= 1 and int(user[2]) < 2 and int(user[1]) != 2):
                    user[1] = "2"
                    content = (message.author.mention +
                               " just hit level " + str(user[1]) + "!")
                    await bot.rest.create_message(channel, content)
                    break
                elif (int(user[2]) >= 2 and int(user[2]) < 4 and int(user[1]) != 3):
                    user[1] = "3"
                    content = (message.author.mention +
                               " just hit level " + str(user[1]) + "!")
                    await bot.rest.create_message(channel, content)
                    break
                elif (int(user[2]) >= 4 and int(user[2]) < 6 and int(user[1]) != 4):
                    user[1] = "4"
                    content = (message.author.mention +
                               " just hit level " + str(user[1]) + "!")
                    await bot.rest.create_message(channel, content)
                    break
                elif (int(user[2]) >= 6 and int(user[2]) < 9 and int(user[1]) != 5):
                    user[1] = "5"
                    content = (message.author.mention +
                               " just hit level " + str(user[1]) + "!")
                    await bot.rest.create_message(channel, content)
                    break
                elif (int(user[2]) >= 9 and int(user[2]) < 12 and int(user[1]) != 6):
                    user[1] = "6"
                    content = (message.author.mention +
                               " just hit level " + str(user[1]) + "!")
                    await bot.rest.create_message(channel, content)
                    break
                elif (int(user[2]) >= 12 and int(user[2]) < 16 and int(user[1]) != 7):
                    user[1] = "7"
                    content = (message.author.mention +
                               " just hit level " + str(user[1]) + "!")
                    await bot.rest.create_message(channel, content)
                    break
                elif (int(user[2]) >= 16 and int(user[2]) < 20 and int(user[1]) != 8):
                    user[1] = "8"
                    content = (message.author.mention +
                               " just hit level " + str(user[1]) + "!")
                    await bot.rest.create_message(channel, content)
                    break
                elif (int(user[2]) >= 20 and int(user[2]) < 25 and int(user[1]) != 9):
                    user[1] = "9"
                    content = (message.author.mention +
                               " just hit level " + str(user[1]) + "!")
                    await bot.rest.create_message(channel, content)
                    break
                elif (int(user[2]) >= 25 and int(user[2]) < 30 and int(user[1]) != 10):
                    user[1] = "10"
                    content = (message.author.mention +
                               " just hit level " + str(user[1]) + "!")
                    await bot.rest.create_message(channel, content)
                    break
                elif (int(user[2]) >= 30 and int(user[2]) < 36 and int(user[1]) != 11):
                    user[1] = "11"
                    content = (message.author.mention +
                               " just hit level " + str(user[1]) + "!")
                    await bot.rest.create_message(channel, content)
                    break
                elif (int(user[2]) >= 36 and int(user[2]) < 42 and int(user[1]) != 12):
                    user[1] = "12"
                    content = (message.author.mention +
                               " just hit level " + str(user[1]) + "!")
                    await bot.rest.create_message(channel, content)
                    break
                elif (int(user[2]) >= 42 and int(user[2]) < 49 and int(user[1]) != 13):
                    user[1] = "13"
                    content = (message.author.mention +
                               " just hit level " + str(user[1]) + "!")
                    await bot.rest.create_message(channel, content)
                    break
                elif (int(user[2]) >= 49 and int(user[2]) < 56 and int(user[1]) != 14):
                    user[1] = "14"
                    content = (message.author.mention +
                               " just hit level " + str(user[1]) + "!")
                    await bot.rest.create_message(channel, content)
                    break
                elif (int(user[2]) >= 56 and int(user[2]) < 64 and int(user[1]) != 15):
                    user[1] = "15"
                    content = (message.author.mention +
                               " just hit level " + str(user[1]) + "!")
                    await bot.rest.create_message(channel, content)
                    break
                elif (int(user[2]) >= 64 and int(user[2]) < 72 and int(user[1]) != 16):
                    user[1] = "16"
                    content = (message.author.mention +
                               " just hit level " + str(user[1]) + "!")
                    await bot.rest.create_message(channel, content)
                    break
                elif (int(user[2]) >= 72 and int(user[2]) < 81 and int(user[1]) != 17):
                    user[1] = "17"
                    content = (message.author.mention +
                               " just hit level " + str(user[1]) + "!")
                    await bot.rest.create_message(channel, content)
                    break
                elif (int(user[2]) >= 81 and int(user[2]) < 90 and int(user[1]) != 18):
                    user[1] = "18"
                    content = (message.author.mention +
                               " just hit level " + str(user[1]) + "!")
                    await bot.rest.create_message(channel, content)
                    break
                elif (int(user[2]) >= 90 and int(user[2]) < 100 and int(user[1]) != 19):
                    user[1] = "19"
                    content = (message.author.mention +
                               " just hit level " + str(user[1]) + "!")
                    await bot.rest.create_message(channel, content)
                    break
                elif (int(user[2]) >= 100 and int(user[1]) != 20):
                    user[1] = "20"
                    content = (message.author.mention +
                               " just hit level " + str(user[1]) + "!")
                    await bot.rest.create_message(channel, content)
                    break
                else:
                    break


@ bot.listen(hikari.GuildReactionDeleteEvent)
async def reaction_del(event: hikari.GuildReactionDeleteEvent) -> None:
    emoji_name = event.emoji_name
    channel_id = event.channel_id
    message_id = event.message_id
    message = await bot.rest.fetch_message(channel_id, message_id)
    author = str(message.author.id)
    if emoji_name == "retweet":
        for user in users:
            if str(user[0]) == author:
                user[2] = int(user[2])-1


@ bot.listen(lightbulb.CommandErrorEvent)
async def on_error(event: lightbulb.CommandErrorEvent) -> None:
    if isinstance(event.exception, lightbulb.CommandInvocationError):
        await event.context.respond(f"Something went wrong during invocation of command `{event.context.command.name}`.")
        raise event.exception

    # Unwrap the exception to get the original cause
    exception = event.exception.__cause__ or event.exception

    if isinstance(exception, lightbulb.NotOwner):
        await event.context.respond("You are not the owner of this bot.")
    elif isinstance(exception, lightbulb.CommandIsOnCooldown):
        await event.context.respond(f"This command is on cooldown. Retry in `{exception.retry_after:.2f}` seconds.")
    elif isinstance(exception, lightbulb.MissingRequiredRole):
        await event.context.respond("You are missing one or more roles required in order to run this command!")
    else:
        raise exception


@bot.command  # COMMAND
@lightbulb.add_checks(lightbulb.has_roles(config.admin_role_id))
@lightbulb.option("user", "user", type=hikari.User)
@lightbulb.command("kick", "Kick Command!")
@lightbulb.implements(lightbulb.SlashCommand)
async def kick(ctx: lightbulb.Context) -> None:
    await bot.rest.kick_user(config.test_guild_id, ctx.options.user.id)
    await ctx.respond(ctx.options.user.mention + " was kicked!")


# Update Member Count
# every 10 minutes (be careful testing with low numbers, i can get rate-limited)
@ tasks.task(m=10, auto_start=True)
async def update_member_count():
    members = await bot.rest.fetch_members(config.test_guild_id)
    await bot.rest.edit_channel(config.total_members_id, name="Total Members: " + str(len(members)))

tasks.load(bot)  # Load Tasks

bot.run()
