
dll_str = '''24a8a6a8f40 : Assembly-CSharp.dll
		24ad3ae91e0 : Assets.Scripts.Utils.ObjectCache.Id
			static fields
			fields
			methods
			base_class
		24a8b5c7ce0 : Assets.Scripts.Utils.SizedListPool.PooledSizedList<T>
			static fields
			fields
			methods
			base_class
		24a8a6db1d0 : Assets.Scripts.Utils.SortedSizedList.SortFunction<T>
			static fields
			fields
			methods
			base_class
		24ad3ae7560 : Assets.Scripts.Utils.UnityHelpers.ResourceUsage
			static fields
			fields
			methods
			base_class
		24ad3a727a0 : AudioJukeBox
			static fields
			fields
				18 : trophyPrefix (type: System.String)
				20 : mainTitleBGM (type: System.String)
				28 : musicTrackData (type: System.Collections.Generic.List<Assets.Scripts.Data.Music.MusicItem>)
			methods
				24ad3d7c3b0 : .ctor () -> System.Void
				24ad3d7c2c0 : GetBossTrack (bossType: Assets.Scripts.Data.Music.BossMusicTrack) -> UnityEngine.AudioClip
				24ad3d7c220 : GetIdFromName (trackName: System.String) -> System.Int32
				24ad3d7c360 : GetMusicItem (trackName: System.String) -> Assets.Scripts.Data.Music.MusicItem
				24ad3d7c180 : GetTitleTheme () -> UnityEngine.AudioClip
				24ad3d7c1d0 : GetTrackByName (trackName: System.String) -> UnityEngine.AudioClip
				24ad3d7c310 : HasPurchasedTrack (trackName: System.String) -> System.Boolean
				24ad3d7c270 : IsFreeTrack (trackName: System.String) -> System.Boolean
				24ad3d7c130 : LoadAsync () -> System.Threading.Tasks.Task
			base_class
				24a8b5233e0 : UnityEngine.ScriptableObject
		24ad3c49140 : AudioPreviewModule
			static fields
			fields
				18 : equalizerAnimator (type: UnityEngine.Animator)
				20 : currentAudioClip (type: UnityEngine.AudioClip)
			methods
				24ad3adec10 : .ctor () -> System.Void
				24ad3adeb70 : PlayEQ (play: System.Int32) -> System.Void
				24ad3adead0 : PlayNewTrack (audioClip: UnityEngine.AudioClip) -> System.Void
				24ad3adeb20 : ShowEQ (show: System.Boolean) -> System.Void
				24ad3adea80 : StopCurrentTrack () -> System.Void
				24ad3adebc0 : Update () -> System.Void
			base_class
				24a8b562980 : UnityEngine.MonoBehaviour
		24ad3e052f0 : BasicIAd
			static fields
			fields
			methods
				24b3ce183b0 : .ctor () -> System.Void
				24b3ce18360 : StartSession () -> System.Void
			base_class
				249677d4d30 : System.Object
		24ad6e724d0 : BlockerZone
			static fields
			fields
				10 : position (type: Assets.Scripts.Simulation.SMath.Vector3)
				1c : radius (type: System.Single)
				20 : inverse (type: System.Boolean)
			methods
				24b6d795a10 : .ctor (position: Assets.Scripts.Simulation.SMath.Vector3, radius: System.Single, inverse: System.Boolean) -> System.Void
			base_class
				249677d4d30 : System.Object
		24ad3f12d30 : BloonProperties
			static fields
			fields
				10 : value__ (type: System.Int32)
			methods
			base_class
				24a8a3f98e0 : System.Enum
		24ad6e742d0 : BloonPropertyHelper
			static fields
			fields
			methods
				24b3cfb5ec0 : DestroysProjectilesIfImmune (bloonProperties: BloonProperties, immuneBloonProperties: BloonProperties) -> System.Boolean
				24b3cfb5f10 : GetBloonTypesConvertedToBloonProperties (bloonPropertiesStr: System.String) -> BloonProperties
				24b3cfb5e20 : GetDamagesTypeConvertedToImmuneBloonProperties (damageTypesStr: System.String, ignoreImmunityForBloonTypesStr: System.String) -> BloonProperties
				24b3cfb5e70 : Log (message: System.String) -> System.Void
			base_class
				249677d4d30 : System.Object
		24ad3a76fa0 : BuildInfo
			static fields
			fields
			methods
				24ad67f1ea0 : Load () -> System.Collections.IEnumerator
				24ad67f1e00 : get_BuildId () -> System.String
				24ad67f1e50 : set_BuildId (value: System.String) -> System.Void
			base_class
				249677d4d30 : System.Object
		24ad3e0ebf0 : CameraSort
			static fields
			fields
				18 : sortMode (type: UnityEngine.TransparencySortMode)
			methods
				24ad3ec0500 : .ctor () -> System.Void
				24ad3ec04b0 : Awake () -> System.Void
			base_class
				24a8b562980 : UnityEngine.MonoBehaviour
		24ad6b9b140 : ChangeAreaTypeMutator
			static fields
			fields
				70 : areaType (type: Assets.Scripts.Models.Map.AreaType)
			methods
				24b3ce18250 : .ctor (areaType: Assets.Scripts.Models.Map.AreaType) -> System.Void
				24b3ce18200 : Mutate (baseModel: Assets.Scripts.Models.Model, model: Assets.Scripts.Models.Model) -> System.Boolean
			base_class
				24ad3aa05f0 : Assets.Scripts.Simulation.Objects.BehaviorMutator
		24ad3e08ef0 : ClockTimeAnimator
			static fields
			fields
				18 : hourHand (type: UnityEngine.GameObject)
				20 : minuteHand (type: UnityEngine.GameObject)
				28 : secondHand (type: UnityEngine.GameObject)
				30 : timeLastUpdated (type: System.Single)
				34 : updateInterval (type: System.Single)
			methods
				24ad3e3ab20 : .ctor () -> System.Void
				24ad3e3aa80 : Start () -> System.Void
				24ad3e3aad0 : Update () -> System.Void
			base_class
				24a8b562980 : UnityEngine.MonoBehaviour
		24ad6b9c4c0 : CommentAttribute
			static fields
			fields
				10 : tooltip (type: System.String)
				18 : comment (type: System.String)
				20 : boxHeight (type: System.Int32)
			methods
				24b6d796df0 : .ctor (comment: System.String, tooltip: System.String, boxHeight: System.Int32) -> System.Void
			base_class
				24a8a703c00 : UnityEngine.PropertyAttribute
		24ad3e15c70 : ContinueGamePanel
			static fields
			fields
				18 : lblDetails (type: TMPro.TMP_Text)
				20 : settings (type: Assets.Scripts.Unity.Menu.GameMenuWithSettings)
			methods
				24ad3e81bf0 : .ctor () -> System.Void
				24ad3e81b50 : CancelLoad () -> System.Void
				24ad3e81b00 : ContinueClicked () -> System.Void
				24ad3e81ba0 : ContinueSavedGame () -> System.Void
				24ad3e81ab0 : Initialise () -> System.Void
			base_class
				24a8b562980 : UnityEngine.MonoBehaviour
		24ad3c47dc0 : CoopMonkeyMoneyLabel
			static fields
			fields
				18 : largeTxt (type: TMPro.TextMeshProUGUI)
				20 : monkeyMoneyIconLarge (type: UnityEngine.GameObject)
				28 : monkeyMoneyIconSmall (type: UnityEngine.GameObject)
				30 : smallTxt (type: TMPro.TextMeshProUGUI)
				38 : settings (type: Assets.Scripts.Unity.Menu.GameMenuWithSettings)
			methods
				24ad3ce7d00 : .ctor () -> System.Void
				24ad3ce7cb0 : GetParentModeButton (transform: UnityEngine.Transform) -> Assets.Scripts.Unity.UI_New.Main.ModeSelect.ModeButton
				24ad3ce7c60 : Initialise () -> System.Void
			base_class
				24a8b562980 : UnityEngine.MonoBehaviour
		24ad3a754a0 : CosmeticHelper
			static fields
				0 : ownPlayerId (type: System.Int32)
				8 : coopPlayerCosmetics (type: System.Collections.Generic.Dictionary<System.Int32,Assets.Scripts.Models.PlayerCosmeticInfo>)
				10 : coopPlayerBloonMods (type: System.Collections.Generic.Dictionary<System.Int32,CosmeticHelper.PlayerBloonMods>)
				18 : coopPlayerIndices (type: System.Collections.Generic.List<System.Int32>)
				20 : rootGameModel (type: Assets.Scripts.Models.GameModel)
				28 : orgTowerModels (type: Assets.Scripts.Models.Towers.TowerModel[])
				30 : orgPowerModels (type: Assets.Scripts.Models.Powers.PowerModel[])
				38 : coopNamedMonkeys (type: System.Collections.Generic.Dictionary<System.Int32,System.Collections.Generic.Dictionary<System.String,System.String>>)
			fields
			methods
				24b6d861e20 : .cctor () -> System.Void
				24b6d861470 : AddBloonAssetChange (cosmetics: Assets.Scripts.Models.PlayerCosmeticInfo, id: System.String) -> System.Void
				24b6d861510 : AddBloonDecal (cosmetics: Assets.Scripts.Models.PlayerCosmeticInfo, id: System.String) -> System.Void
				24b6d8614c0 : AddBloonPopFX (cosmetics: Assets.Scripts.Models.PlayerCosmeticInfo, id: System.String) -> System.Void
				24b6d861420 : AddPet (cosmetics: Assets.Scripts.Models.PlayerCosmeticInfo, id: System.String) -> System.Void
				24b6d861560 : AddPowerAssetChange (cosmetics: Assets.Scripts.Models.PlayerCosmeticInfo, id: System.String) -> System.Void
				24b6d8615b0 : AddProp (cosmetics: Assets.Scripts.Models.PlayerCosmeticInfo, id: System.String) -> System.Void
				24b6d8613d0 : AddTowerAssetChange (cosmetics: Assets.Scripts.Models.PlayerCosmeticInfo, id: System.String) -> System.Void
				24b6d861b50 : ApplyAssetChangesToBloonModel (bloonModel: Assets.Scripts.Models.Bloons.BloonModel, bloonCosData: Assets.Scripts.Data.Cosmetics.BloonAssetChanges.BloonAssetChange) -> System.Void
				24b6d861c40 : ApplyAssetChangesToPowerModel (pm: Assets.Scripts.Models.Powers.PowerModel, pac: Assets.Scripts.Data.Cosmetics.PowerAssetChanges.PowerAssetChange) -> System.Void
				24b6d861a60 : ApplyAssetChangesToTowerModel (tm: Assets.Scripts.Models.Towers.TowerModel, assetChangeIds: System.Collections.Generic.IEnumerable<System.String>) -> System.Void
				24b6d861920 : ApplyCoopPlayerCosmeticsToPowerModel (powerModel: Assets.Scripts.Models.Powers.PowerModel, inputId: System.Int32) -> Assets.Scripts.Models.Powers.PowerModel
				24b6d8618d0 : ApplyCoopPlayerCosmeticsToTowerModel (towerModel: Assets.Scripts.Models.Towers.TowerModel, inputId: System.Int32) -> Assets.Scripts.Models.Towers.TowerModel
				24b6d8619c0 : ApplyCosmeticsToBloonModels (bloonModels: Assets.Scripts.Models.Bloons.BloonModel[], data: Assets.Scripts.Models.PlayerCosmeticInfo) -> System.Void
				24b6d861880 : ApplyCosmeticsToGameModel (data: Assets.Scripts.Models.PlayerCosmeticInfo) -> System.Void
				24b6d861970 : ApplyCosmeticsToTowerModel (towerModel: Assets.Scripts.Models.Towers.TowerModel, data: Assets.Scripts.Models.PlayerCosmeticInfo) -> System.Void
				24b6d861bf0 : ApplyDecalToBloonModel (bloonModel: Assets.Scripts.Models.Bloons.BloonModel, bloonDecal: Assets.Scripts.Data.Cosmetics.BloonDecals.BloonDecalSwap, displayLayer: System.Int32) -> System.Void
				24b6d861ab0 : ApplyPetToTowerModel (tm: Assets.Scripts.Models.Towers.TowerModel, id: System.String) -> System.Void
				24b6d861ba0 : ApplyPopFXToBloonModel (bloonModel: Assets.Scripts.Models.Bloons.BloonModel, bloonPopFXSwap: Assets.Scripts.Data.Cosmetics.BloonPopFXs.BloonPopFX) -> System.Void
				24b6d861b00 : ApplyPropsToTowerModel (tm: Assets.Scripts.Models.Towers.TowerModel, ids: System.Collections.Generic.IEnumerable<System.String>) -> System.Void
				24b6d861a10 : ApplyTowerSkinToTowerModel (towerModel: Assets.Scripts.Models.Towers.TowerModel, data: Assets.Scripts.Models.Skins.SkinModel) -> System.Void
				24b6d8617e0 : CleanUp () -> System.Void
				24b6d861600 : ClearCosmeticsForCoopPlayers () -> System.Void
				24b6d8616f0 : CreateBloonModsForPlayer (inputId: System.Int32) -> CosmeticHelper.PlayerBloonMods
				24b6d861790 : GetBloonModel (id: System.String, emissionIndex: System.Int32, useRootModel: System.Boolean) -> Assets.Scripts.Models.Bloons.BloonModel
				24b6d861c90 : GetHeroEmote (heroId: System.String, skinId: System.String, smallEmote: System.Boolean) -> Assets.Scripts.Utils.SpriteReference
				24b6d861d30 : GetMonkeyName (inputId: System.Int32, monkeyKey: System.String) -> System.String
				24b6d861380 : GetPlayerCosmetics (playerData: Assets.Scripts.Models.Profile.ProfileModel) -> Assets.Scripts.Models.PlayerCosmeticInfo
				24b6d861830 : Init (gameModel: Assets.Scripts.Models.GameModel) -> System.Void
				24b6d861740 : RefreshBloonModelsForAllPlayers () -> System.Void
				24b6d861650 : RemoveCosmeticsForCoopPlayer (inputId: System.Int32) -> System.Void
				24b6d8616a0 : SetCosmeticsForCoopPlayer (inputId: System.Int32, cosmetics: Assets.Scripts.Models.PlayerCosmeticInfo) -> System.Void
				24b6d861ce0 : SetMonkeyNamesForCoopPlayer ? - (System.Int32,System.Collections.Generic.Dictionary<System.String,System.String>) -> System.Void
				24b6d861d80 : SwapDarkTempleAsset (str: System.String) -> System.String
				24b6d861dd0 : SwapDarkTempleAsset (reference: Assets.Scripts.Utils.SpriteReference) -> Assets.Scripts.Utils.SpriteReference
			base_class
				249677d4d30 : System.Object
		24ad3a74d20 : CosmeticHelper.PlayerBloonMods
			static fields
			fields
				10 : bloonsByName (type: System.Collections.Generic.Dictionary<System.String,Assets.Scripts.Models.Bloons.BloonModel>)
			methods
				24b6d797210 : .ctor () -> System.Void
			base_class
				249677d4d30 : System.Object
		24ad343e970 : CustomAnimationComponent
			static fields
			fields
				18 : target (type: UnityEngine.GameObject)
				20 : duration (type: System.Single)
				28 : curve (type: UnityEngine.AnimationCurve)
				30 : isPlaying (type: System.Boolean)
				31 : loop (type: System.Boolean)
				32 : disableOnEnd (type: System.Boolean)
				33 : stopPlayingOnEnd (type: System.Boolean)
				34 : resetOnEnable (type: System.Boolean)
				35 : updateAnimOnReset (type: System.Boolean)
				38 : speedMultiplier (type: System.Single)
				3c : useUnscaledTime (type: System.Boolean)
				40 : targetTransform (type: UnityEngine.Transform)
				48 : elapsed (type: System.Single)
			methods
				24ad3c017c0 : .ctor () -> System.Void
				24ad3c01590 : Awake () -> System.Void
				24ad3c01630 : DisableIfInvalid () -> System.Boolean
				24ad3c01770 : OnEnable () -> System.Void
				24ad3c01720 : Reset () -> System.Void
				24ad3c01680 : Trigger () -> System.Void
				24ad3c015e0 : Update () -> System.Void
				24ad3c016d0 : UpdateAnimation (currentTime: System.Single) -> System.Void
			base_class
				24a8b562980 : UnityEngine.MonoBehaviour
		24ad3dbd0e0 : CustomColorAnimator
			static fields
			fields
				50 : color1 (type: UnityEngine.Color)
				60 : color2 (type: UnityEngine.Color)
				70 : targetSprite (type: UnityEngine.SpriteRenderer)
				78 : img (type: UnityEngine.UI.Image)
			methods
				24ad3ce8f00 : .ctor () -> System.Void
				24ad3ce8e60 : Start () -> System.Void
				24ad3ce8eb0 : UpdateAnimation (currentTime: System.Single) -> System.Void
			base_class
				24ad343e970 : CustomAnimationComponent
		24ad3e4c360 : CustomFlyoverAnimator
			static fields
			fields
				50 : startPoint (type: UnityEngine.Vector3)
				5c : endPoint (type: UnityEngine.Vector3)
				68 : approachDistance (type: System.Single)
			methods
				24ad3dc50e0 : .ctor () -> System.Void
				24ad3dc4f50 : Awake () -> System.Void
				24ad3dc4fa0 : OnDisable () -> System.Void
				24ad3dc4ff0 : Reset () -> System.Void
				24ad3dc5040 : SetInitialPosition () -> System.Void
				24ad3dc5090 : UpdateAnimation (currentTime: System.Single) -> System.Void
			base_class
				24ad343e970 : CustomAnimationComponent
		24ad3c6f160 : CustomMoveAnimator
			static fields
			fields
				50 : startOffset (type: UnityEngine.Vector3)
				5c : endOffset (type: UnityEngine.Vector3)
				68 : homePosition (type: UnityEngine.Vector3)
			methods
				24ad3558640 : .ctor () -> System.Void
				24ad35585a0 : Start () -> System.Void
				24ad35585f0 : UpdateAnimation (currentTime: System.Single) -> System.Void
			base_class
				24ad343e970 : CustomAnimationComponent
		24ad3c40bc0 : CustomPlayableAnimatorTest
			static fields
			fields
				18 : playableAnimator (type: Assets.Scripts.Unity.Display.Animation.PlayableAnimator)
				20 : clipConfigs (type: System.Collections.Generic.List<Assets.Scripts.Unity.Display.Animation.CustomAnimationClipConfig>)
			methods
				24ad3ce6200 : .ctor () -> System.Void
				24ad3ce6160 : Start () -> System.Void
				24ad3ce61b0 : Update () -> System.Void
			base_class
				24a8b562980 : UnityEngine.MonoBehaviour
		24ad3c43140 : CustomRendererToggleAnimator
			static fields
			fields
				18 : targetRenderer (type: UnityEngine.Renderer)
				20 : duration (type: System.Single)
				28 : curve (type: UnityEngine.AnimationCurve)
				30 : isPlaying (type: System.Boolean)
				31 : loop (type: System.Boolean)
				34 : elapsed (type: System.Single)
			methods
				24ad3d4a5e0 : .ctor () -> System.Void
				24ad3d4a4f0 : Start () -> System.Void
				24ad3d4a540 : Update () -> System.Void
				24ad3d4a590 : UpdateToggle (currentTime: System.Single) -> System.Void
			base_class
				24a8b562980 : UnityEngine.MonoBehaviour
		24ad343f5b0 : CustomRotationAnimator
			static fields
			fields
				50 : rotationsPerDuration (type: System.Single)
				54 : axis (type: CustomRotationAnimator.Axis)
				58 : useLocalCoordinateSustem (type: System.Boolean)
				59 : randomizeAngle (type: System.Boolean)
				5a : randomizeSpeed (type: System.Boolean)
				60 : randomSpeedMultiplierRange (type: RangeValue)
				68 : angleOffset (type: System.Single)
				6c : rotationAxis (type: UnityEngine.Vector3)
			methods
				24ad3e3ac20 : .ctor () -> System.Void
				24ad3e3ab80 : Start () -> System.Void
				24ad3e3abd0 : UpdateAnimation (currentTime: System.Single) -> System.Void
			base_class
				24ad343e970 : CustomAnimationComponent
		24ad3a8a300 : CustomRotationAnimator.Axis
			static fields
			fields
				10 : value__ (type: System.Int32)
			methods
			base_class
				24a8a3f98e0 : System.Enum
		24ad3c3d440 : CustomRotationSimple
			static fields
			fields
				18 : target (type: UnityEngine.GameObject)
				20 : rotationAxis (type: UnityEngine.Vector3)
				2c : useLocalCoordinates (type: System.Boolean)
				30 : speed (type: System.Single)
				34 : minStartingOffset (type: System.Single)
				38 : maxStartingOffset (type: System.Single)
				3c : angle (type: System.Single)
				40 : startingAngle (type: System.Single)
			methods
				24ad3ce5c00 : .ctor () -> System.Void
				24ad3ce5b60 : Start () -> System.Void
				24ad3ce5bb0 : Update () -> System.Void
			base_class
				24a8b562980 : UnityEngine.MonoBehaviour
		24ad3eca830 : CustomScaleAnimator
			static fields
			fields
			methods
				24ad3e39520 : .ctor () -> System.Void
				24ad3e394d0 : StopPlaying () -> System.Void
				24ad3e39480 : UpdateAnimation (currentTime: System.Single) -> System.Void
			base_class
				24ad343e970 : CustomAnimationComponent
		24ad3e01ff0 : DanceFloor
			static fields
			fields
				18 : uvAnimationTileX (type: System.Int32)
				1c : uvAnimationTileY (type: System.Int32)
				20 : framesPerSecond (type: System.Single)
				24 : currentTimeInt (type: System.Int32)
				28 : randomNumX (type: System.Int32)
				2c : randomNumY (type: System.Int32)
				30 : offset (type: UnityEngine.Vector2)
				38 : _myRenderer (type: UnityEngine.Renderer)
			methods
				24ad3ce6100 : .ctor () -> System.Void
				24ad3ce6060 : Start () -> System.Void
				24ad3ce60b0 : Update () -> System.Void
			base_class
				24a8b562980 : UnityEngine.MonoBehaviour
		24ad3b1f4b0 : DebugSetParagonLevel
			static fields
			fields
			methods
				24ad3412480 : .ctor () -> System.Void
			base_class
				24a8b562980 : UnityEngine.MonoBehaviour
		24ad3e067f0 : DebugTemplePoints
			static fields
			fields
			methods
				24ad3415a80 : .ctor () -> System.Void
			base_class
				24a8b562980 : UnityEngine.MonoBehaviour
		24ad3e0a6f0 : DeepCompare
			static fields
			fields
				10 : bindFlags (type: System.Reflection.BindingFlags)
				18 : processedObjectsA (type: System.Collections.Generic.HashSet<System.Object>)
				20 : processedObjectsB (type: System.Collections.Generic.HashSet<System.Object>)
			methods
				24b3cfb6c30 : .ctor () -> System.Void
				24b3cfb6be0 : Compare (a: System.Object, b: System.Object) -> System.Boolean
				24b3cfb6b90 : GetCheckCount () -> System.Int32
				24b3cfb6b40 : NullCheck (a: System.Object, b: System.Object) -> System.Boolean
			base_class
				249677d4d30 : System.Object
		24ad3c3eac0 : DestroyComponent
			static fields
			fields
			methods
				24ad3ca6a30 : .ctor () -> System.Void
				24ad3ca69e0 : TriggerDestroy () -> System.Void
			base_class
				24a8b562980 : UnityEngine.MonoBehaviour
		24ad3e094f0 : DifficultyCollectionEventItemLabel
			static fields
			fields
				18 : difficultyType (type: System.String)
				20 : settings (type: Assets.Scripts.Unity.Menu.GameMenuWithSettings)
			methods
				24ad3e52090 : .ctor () -> System.Void
				24ad3e52040 : Initiailise () -> System.Void
			base_class
				24a8b562980 : UnityEngine.MonoBehaviour
		24ad3e02470 : DifficultyCollectionEventItems
			static fields
			fields
				18 : difficultyCollectionEventItemLabels (type: DifficultyCollectionEventItemLabel[])
			methods
				24ad3da0fa0 : .ctor () -> System.Void
				24ad3da0f50 : Initialise () -> System.Void
			base_class
				24a8b562980 : UnityEngine.MonoBehaviour
		24ad3e03df0 : DifficultySelectMmItems
			static fields
				0 : modeUnlocks (type: System.Collections.Generic.Dictionary<System.String,System.String>)
			fields
				18 : monkeyMoneyIconLarge (type: UnityEngine.GameObject)
				20 : largeTxt (type: TMPro.TextMeshProUGUI)
				28 : monkeyMoneyIconSmall (type: UnityEngine.GameObject)
				30 : smallTxt (type: TMPro.TextMeshProUGUI)
				38 : difficulty (type: System.String)
				40 : settings (type: Assets.Scripts.Unity.Menu.GameMenuWithSettings)
			methods
				24ad3dd5710 : .cctor () -> System.Void
				24ad3dd56c0 : .ctor () -> System.Void
				24ad3dd5620 : GetModeUnlock (mode: System.String) -> System.String
				24ad3dd5670 : GetModes (difficulty: System.String) -> System.Collections.Generic.List<System.String>
				24ad3dd55d0 : Initialise () -> System.Void
			base_class
				24a8b562980 : UnityEngine.MonoBehaviour
		24ad3c38940 : DifficultySpritesAsset
			static fields
			fields
				18 : difficultyBadgeSprites (type: Assets.Scripts.Utils.SpriteReference[])
			methods
				24ad3414b20 : .ctor () -> System.Void
			base_class
				24a8b5233e0 : UnityEngine.ScriptableObject
		24ad3e02d70 : DigitalClockFaceAnimator
			static fields
			fields
				18 : text (type: TMPro.TextMeshPro)
				20 : time (type: System.Single)
				24 : seconds (type: System.Int32)
			methods
				24ad3da1890 : .ctor () -> System.Void
				24ad3da1840 : Update () -> System.Void
			base_class
				24a8b562980 : UnityEngine.MonoBehaviour
'''