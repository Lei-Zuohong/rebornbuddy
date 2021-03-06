using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;
using Clio.Utilities;
using Clio.XmlEngine;
using ff14bot.Behavior;
using ff14bot.Helpers;
using ff14bot.Managers;
using ff14bot.Navigation;
using ff14bot.NeoProfiles;
using ff14bot.RemoteWindows;
using TreeSharp;
using Action = TreeSharp.Action;

namespace ff14bot.NeoProfiles
{
    [XmlElement("SelectStringClick")]

    public class SelectStringClickTag : ProfileBehavior
    {
        private bool _done;

        [DefaultValue("")]
        [XmlAttribute("Contains")]
        public string contains { get; set; }

        [DefaultValue(255)]
        [XmlAttribute("Slot")]
        public int slot { get; set; }

        public override bool IsDone { get { return _done; } }

        protected override Composite CreateBehavior()
        {
            return new PrioritySelector(
                new Decorator(ret => !RemoteWindows.SelectString.IsOpen,
                    new ActionAlwaysSucceed()
                ),
                new Decorator(ret => RemoteWindows.SelectString.IsOpen,
                    new Action(r =>
                    {
                        if (contains != "")
                        {
                            RemoteWindows.SelectString.ClickLineContains(contains);
                        }
                        if (slot != 255)
                        {
                            RemoteWindows.SelectString.ClickSlot(System.Convert.ToUInt32(slot));
                        }
                        _done = true;
                    })
                )
            );
        }

        /// <summary>
        /// This gets called when a while loop starts over so reset anything that is used inside the IsDone check
        /// </summary>
        protected override void OnResetCachedDone()
        {
            _done = false;
        }

        protected override void OnDone()
        {

        }
    }
}