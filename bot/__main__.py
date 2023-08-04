import lightbulb

from bot import constants

bot = lightbulb.BotApp(constants.Bot.token, default_enabled_guilds=(934896901256515714))


@bot.command
@lightbulb.command("whoami", "Checks who you are")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None:
    await ctx.respond(ctx.author.username)


bot.run()
