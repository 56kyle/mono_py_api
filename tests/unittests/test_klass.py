
import pytest
from src.klass import Klass




class TestKlass:
    def test_simple_klass(self):
        Klass(line='\t\t\t\t10 : dimensions (type: System.Int32)\n')

    def test_klass_with_generic_type(self):
        Klass(line='\t\t\t\t0 : Item1 (type: T1)\n')

    def test_klass_with_type_containing_generic(self):
        Klass(line='\t\t\t\t18 : values (type: System.Object[])\n')


class TestKlassMixins:
    @pytest.fixture(scope='class')
    def klass(self):
        return Klass(lines=[
            '\t\t24ad3c2cac0 : Assets.Scripts.Unity.UI_New.CommonForegroundScreen\n',
            '\t\t\tstatic fields\n',
            '\t\t\t\t0 : instance (type: Assets.Scripts.Unity.UI_New.CommonForegroundScreen)\n',
            '\t\t\tfields\n',
            '\t\t\t\t18 : animator (type: UnityEngine.Animator)\n',
            '\t\t\t\t20 : heading (type: UnityEngine.GameObject)\n',
            '\t\t\t\t28 : backButton (type: UnityEngine.GameObject)\n',
            '\t\t\t\t30 : monkeyMoney (type: UnityEngine.GameObject)\n',
            '\t\t\t\t38 : knownledge (type: UnityEngine.GameObject)\n',
            '\t\t\t\t40 : changeHeroButton (type: UnityEngine.GameObject)\n',
            '\t\t\t\t48 : lblHeading (type: TMPro.TextMeshProUGUI)\n',
            '\t\t\t\t50 : buyMoreMonkeyMoneyButton (type: UnityEngine.GameObject)\n',
            '\t\t\t\t58 : buyKnowledgeButton (type: UnityEngine.GameObject)\n',
            '\t\t\t\t60 : lblKnowledge (type: TMPro.TextMeshProUGUI)\n',
            '\t\t\t\t68 : loadingImg (type: UnityEngine.UI.Image)\n',
            '\t\t\t\t70 : backEnabled (type: System.Boolean)\n',
            '\t\t\t\t74 : knowledgePoints (type: System.Int32)\n',
            '\t\t\tmethods\n',
            '\t\t\t\t24ad3dec0f0 : .cctor () -> System.Void\n',
            '\t\t\t\t24ad3dec0a0 : .ctor () -> System.Void\n',
            '\t\t\t\t24ad3debbf0 : Awake () -> System.Void\n',
            '\t\t\t\t24ad3debf10 : BackButtonClicked () -> System.Void\n',
            '\t\t\t\t24ad3debfb0 : BuyKnowledgeClicked () -> System.Void\n',
            '\t\t\t\t24ad3dec000 : ChangeHeroButtonClicked () -> System.Void\n',
            '\t\t\t\t24ad3debce0 : Hide () -> System.Void\n',
            '\t\t\t\t24ad3debd30 : IsBackEnabled () -> System.Boolean\n',
            '\t\t\t\t24ad3debf60 : MoreMonkeyMoneyClicked () -> System.Void\n',
            '\t\t\t\t24ad3debc40 : OnDestroy () -> System.Void\n',
            '\t\t\t\t24ad3debc90 : Show (showBackButton: System.Boolean, heading: System.String, showMonkeyMoney: System.Boolean, enableBuyMonkeyMoney: System.Boolean, showKnowledge: System.Boolean, showBuyKnowledge: System.Boolean, showChangeHeroButton: System.Boolean) -> System.Void\n',
            '\t\t\t\t24ad3debd80 : ShowHideBackButton (showBackButton: System.Boolean) -> System.Void\n',
            '\t\t\t\t24ad3debdd0 : ShowHideHeroButton (showHeroButton: System.Boolean) -> System.Void\n',
            '\t\t\t\t24ad3debe70 : ShowHideKnowledge (show: System.Boolean) -> System.Void\n',
            '\t\t\t\t24ad3debe20 : ShowHideMonkeyMoney (show: System.Boolean) -> System.Void\n',
            '\t\t\t\t24ad3debec0 : ShowLobbyMessage (show: System.Boolean) -> System.Void\n',
            '\t\t\t\t24ad3dec050 : Update () -> System.Void\n',
            '\t\t\tbase_class\n',
            '\t\t\t\t24a8b562980 : UnityEngine.MonoBehaviour\n'
        ])

    def test_klass_is_memorable(self, klass: Klass):
        assert klass.address == '10'

    def test_klass_is_parseable(self, klass: Klass):
        assert klass.line == '\t\t\t\t10 : dimensions (type: System.Object[])\n'
        assert klass.lines is None
        assert klass.as_line() == '\t\tself.dimensions: List[System.Object] = dimensions'


