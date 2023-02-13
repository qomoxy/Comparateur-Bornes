import pygame
from Abilities.abilities import RangedAbility, AbilityInfo, AbilityProperties, AbilityShape
from Abilities.abilityEffects import EffectManager
from Entities.Enemies.enemy import EnemyProperties
from Entities.entity import Entity
from Base.animations import Animation

# region Slime
__slimeIdleAnim = Animation(
    spriteSheet=pygame.image.load("Sprites/slime.png"),
    loop=True, length=.6,
    sheetSpriteCount=(12, 1), spriteAnchor=(0, .5),
    startEndFrames=(0, 1))

__slimeJumpAnim = Animation(
    spriteSheet=pygame.image.load("Sprites/slime.png"),
    loop=False, length=1.2,
    sheetSpriteCount=(12, 1), spriteAnchor=(0, .5),
    startEndFrames=(2, 11))

__slimeJumpAbilityInfo = AbilityInfo("Saut", "Boing !", __slimeJumpAnim)
__slimeJumpAbilityProperties = AbilityProperties((2, 6), (2, 4), (0, 0))

__slimeJumpShape = AbilityShape(["🟥⬜🟥",
                                 "⬜🔲⬜",
                                 "🟥⬜🟥"],
                                "Red")
__slimeJumpZone = AbilityShape(["⬜⬜⬜",
                                "⬜🔲⬜",
                                "⬜⬜⬜"],
                               "Red")

__slimeEffects = EffectManager([])

__slimeJumpAbility = RangedAbility(
    __slimeJumpAbilityProperties, __slimeJumpAbilityInfo, __slimeEffects, __slimeJumpShape, __slimeJumpZone)

__slimeEntity = Entity(5, "Slime", "Un slime", (32, 32), [
                       __slimeJumpAbility], (0, 3), (0, 3))

slimeEnemyProperties = EnemyProperties(__slimeEntity, __slimeIdleAnim)
# endregion
