import lightbulb

from bot import constants

bot = lightbulb.BotApp(
    constants.Bot.token,
    ignore_bots=True,
    owner_ids=constants.Bot.owner_ids,
    default_enabled_guilds=constants.Bot.default_enabled_guilds,
)


@bot.command
@lightbulb.command("whoami", "Checks who you are")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None:
    await ctx.respond(ctx.author.username)


bot.run()
