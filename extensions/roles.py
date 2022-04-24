import lightbulb
import hikari
import config

plugin = lightbulb.Plugin("Roles")


@plugin.command  # ROLES COMMAND
@lightbulb.add_checks(lightbulb.has_roles(config.admin_role_id))
@lightbulb.option("user", "user", type=hikari.User)
@lightbulb.option("role", "role", type=hikari.Role)
@lightbulb.option("option", "give or take", type=str, choices=["give", "take"])
@lightbulb.command("role", "Command that manages Roles!", aliases=["roles", "r"])
@lightbulb.implements(lightbulb.SlashCommand)
async def roles(ctx: lightbulb.Context) -> None:
    if ctx.options.option == "give":
        await ctx.options.user.add_role(ctx.options.role)
        await ctx.respond(ctx.options.user.mention + " was given the " + ctx.options.role.mention + " role!")
    else:
        await ctx.options.user.remove_role(ctx.options.role)
        await ctx.respond("The " + ctx.options.role.mention + " role was taken from " + ctx.options.user.mention + "!")


def load(bot):
    bot.add_plugin(plugin)


def unload(bot):
    bot.remove_plugin(plugin)
