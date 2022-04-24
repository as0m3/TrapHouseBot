import lightbulb

plugin = lightbulb.Plugin("Add")


@plugin.command  # ADD COMMAND
@lightbulb.option('num2', 'The second number', type=int)
@lightbulb.option('num1', 'The first number', type=int)
@lightbulb.command('add', 'Adds two numbers together.')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx: lightbulb.Context) -> None:
    await ctx.respond(ctx.options.num1 + ctx.options.num2)


def load(bot):
    bot.add_plugin(plugin)


def unload(bot):
    bot.remove_plugin(plugin)
