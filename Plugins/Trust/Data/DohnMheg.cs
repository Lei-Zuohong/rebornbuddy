using Buddy.Coroutines;
using Clio.Utilities;
using ff14bot;
using ff14bot.Helpers;
using ff14bot.Managers;
using ff14bot.Navigation;
using ff14bot.Objects;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Media;

namespace Trust
{
    public static class DohnMheg
    {
        public static async Task<bool> Run()
        {

            var plugin = PluginManager.Plugins.Where(p => p.Plugin.Name == "SideStep" || p.Plugin.Name == "回避").First();

            var check = GameObjectManager.GetObjectsOfType<BattleCharacter>().Where(r => r.CastingSpellId != 0 && !r.IsMe && r.Distance() < 50 && (r.CastingSpellId == 15723 || r.CastingSpellId == 13520 || r.CastingSpellId == 13844));
			
			var check2 = GameObjectManager.GetObjectsOfType<BattleCharacter>().Where(r => r.CastingSpellId != 0 && !r.IsMe && r.Distance() < 50 && (r.CastingSpellId == 13552));

            var sC3 = GameObjectManager.GetObjectsOfType<BattleCharacter>().Where(r => !r.IsMe && r.Distance() < 50 && r.NpcId == 8146);  //73BOSS3

            //过独木桥     BOSS 3             
            if (check.Any() == true && sC3.First().Location.Distance2D(Core.Me.Location) >= 10)
            {
                //读条中断
                if (Core.Me.IsCasting) ActionManager.StopCasting();

                await Coroutine.Sleep(3000);
                Logging.Write(Colors.Aquamarine, $"过独木桥");
                //过桥
                var Location = new Vector3("-142.8355,-144.5264,-232.6624");
                while (Location.Distance2D(Core.Me.Location) > 0.2)
                {
                    Logging.Write(Colors.Aquamarine, $"远点距离:{Location.Distance2D(Core.Me.Location)}");
                    Navigator.PlayerMover.MoveTowards(Location);
                    await Coroutine.Sleep(30);
                }
                Location = new Vector3("-140.8284,-144.5366,-246.1443");
                while (Location.Distance2D(Core.Me.Location) > 0.2)
                {
                    Logging.Write(Colors.Aquamarine, $"远点距离:{Location.Distance2D(Core.Me.Location)}");
                    Navigator.PlayerMover.MoveTowards(Location);
                    await Coroutine.Sleep(30);
                }
                Location = new Vector3("-130.1889,-144.5366,-242.384");
                while (Location.Distance2D(Core.Me.Location) > 0.2)
                {
                    Logging.Write(Colors.Aquamarine, $"远点距离:{Location.Distance2D(Core.Me.Location)}");
                    Navigator.PlayerMover.MoveTowards(Location);
                    await Coroutine.Sleep(30);
                }
                Location = new Vector3("-114.455,-144.5366,-244.2632");
                while (Location.Distance2D(Core.Me.Location) > 0.2)
                {
                    Logging.Write(Colors.Aquamarine, $"远点距离:{Location.Distance2D(Core.Me.Location)}");
                    Navigator.PlayerMover.MoveTowards(Location);
                    await Coroutine.Sleep(30);
                }
                Location = new Vector3("-125.6857,-144.5238,-249.264");
                while (Location.Distance2D(Core.Me.Location) > 0.2)
                {
                    Logging.Write(Colors.Aquamarine, $"远点距离:{Location.Distance2D(Core.Me.Location)}");
                    Navigator.PlayerMover.MoveTowards(Location);
                    await Coroutine.Sleep(30);
                }
                Location = new Vector3("-122.5055,-144.5192,-258.3726");
                while (Location.Distance2D(Core.Me.Location) > 0.2)
                {
                    Logging.Write(Colors.Aquamarine, $"远点距离:{Location.Distance2D(Core.Me.Location)}");
                    Navigator.PlayerMover.MoveTowards(Location);
                    await Coroutine.Sleep(30);
                }
                Location = new Vector3("-128.1084,-144.5226,-258.0896");
                while (Location.Distance2D(Core.Me.Location) > 1)
                {
                    Logging.Write(Colors.Aquamarine, $"远点距离:{Location.Distance2D(Core.Me.Location)}");
                    Navigator.PlayerMover.MoveTowards(Location);
                    await Coroutine.Sleep(100);
                }

            }
			
			if (check2.Any() == true)
            {
                Logging.Write(Colors.Aquamarine, $"背对");
                
                var Location = new Vector3("-128.474,-144.5366,-243.2417");
                while (Location.Distance2D(Core.Me.Location) > 1)
                {
                    Logging.Write(Colors.Aquamarine, $"背对:{Location.Distance2D(Core.Me.Location)}");
                    Navigator.PlayerMover.MoveTowards(Location);
                    await Coroutine.Sleep(100);
                }

                Navigator.PlayerMover.MoveStop();
                await Coroutine.Sleep(3000);
            }

            /// 2183, 4708, 4709, 6975, 10384, 10385, 10386, 11768, 13920, 15796, 16227, 16973, 16974, 16975, 17199      :: Savage Swipe
            /// 4526, 11014, 13786, 15794, 16234                                                                         :: Unfinal Sting
            /// 5174, 5175, 13547, 13548                                                                                 :: Corrosive Bile
            /// 5176, 13549                                                                                              :: Malaise
            /// 5177, 13550                                                                                              :: Bile Bombardment
            /// 5178, 5179, 13952, 13953                                                                                 :: Flailing Tentacles
            /// 13514                                                                                                    :: Venom Shower
            /// 13551                                                                                                    :: Toad Choir
            /// 15788, 16837                                                                                             :: Pollen Corona
            HashSet<uint> spellCastIds = new HashSet<uint>()
            {
                2183, 4526, 4708, 4709, 5174, 5175, 5176, 5177, 5178, 5179,
                6975, 10384, 10385, 10386, 11014, 11768, 13514, 13547, 13548,
                13549, 13550, 13551, 13786, 13920, 13952, 13953, 15788, 15794,
                15796, 16227, 16234, 16837, 16973, 16974, 16975, 17199
            };
            bool spellCasting = GameObjectManager.GetObjectsOfType<BattleCharacter>(true, false).Where(obj =>
                spellCastIds.Contains(obj.CastingSpellId) && obj.Distance() < 50).Count() > 0;

            if (spellCasting) { await Helpers.GetClosestAlly.Follow(); }

            if (Core.Target != null)
            {

                var sC = GameObjectManager.GetObjectsOfType<BattleCharacter>().Where(
                    r => !r.IsMe && r.Distance() < 50 && r.NpcId == 8141
                    );  //73BOSS1
				var sC1 = GameObjectManager.GetObjectsOfType<BattleCharacter>().Where(
                    r => !r.IsMe && r.Distance() < 50 && r.NpcId == 8146
                    );  //73BOSS3	

                // 73boss 1 移动 
                if (sC.Any() == true)
                {
                    if (plugin != null)
                    {
                        if (plugin.Enabled == true) plugin.Enabled = false;
                    }

                    Logging.Write(Colors.Aquamarine, $"boss1");
                    var spellCaster = sC.First();


                    if (spellCaster != null && spellCaster.Name == Core.Target.Name)
                    {

                        var Obj = GameObjectManager.GetObjectsOfType<BattleCharacter>(true).Where(r =>
                                    (r.NpcId == 729 || r.NpcId == 8378 ||     // "雅·修特拉"
                                                                              //r.NpcId == 1492 ||                       // "于里昂热"
                                                                              //r.NpcId == 4130 ||                       // "阿尔菲诺"
                                    r.NpcId == 5239 ||                       // "阿莉塞"
                                    r.NpcId == 8889 ||                        // 琳   
                                    r.Name == "雅·修特拉" ||
                                    r.Name == "阿莉塞" ||
									r.Name == "敏菲利亚" ||
                                    r.Name == "琳")
                                    && r.IsDead == false
                                     ).OrderBy(r => r.Distance()).First();

                        //当距离大于跟随距离 再处理跟随
                        if (Obj.Location.Distance2D(Core.Me.Location) >= 0.2)
                        {
                            //读条中断
                            if (Core.Me.IsCasting) ActionManager.StopCasting();
                            
                            // 选中跟随最近的队友
                            Obj.Target();

                            Logging.Write(Colors.Aquamarine, $"队友{Obj.Name}距离:{Obj.Location.Distance2D(Core.Me.Location)}");

                            while (Obj.Location.Distance2D(Core.Me.Location) >= 0.2)
                            {
                                Navigator.PlayerMover.MoveTowards(Obj.Location);
                                await Coroutine.Sleep(50);
                            }
                            Navigator.PlayerMover.MoveStop();
                            await Coroutine.Sleep(50);
                            return true;
                        }

                    }
                }
				if (sC1.Any() == true)
                {
                    if (plugin != null)
                    {
                        if (plugin.Enabled == true) plugin.Enabled = false;
                    }
                }

            }

            return false;

        }
    }

}
