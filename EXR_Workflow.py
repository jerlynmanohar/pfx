import BlackmagicFusion as bmd
from time import sleep


def hosSplit():
    ldr = comp.FindToolByID("Loader")
    flow = comp.CurrentFrame.FlowView
    select_tool = flow.Select(ldr, True)
    make_tool_active = comp.SetActiveTool(ldr)
    composition.RunScript("C:/ProgramData/Blackmagic Design/Fusion/Reactor/Deploy/Scripts/Tool/hos_SplitEXR_Ultra.lua")
    return


def addtool():
    tool_name = comp.GetToolList().values()
    for i in tool_name:
        print(i.GetAttrs('TOOLS_Name'))
    return


def mrge():
    global flow
    diff_direct = comp.diffuse_direct.Output  # get output of node
    diff_indir = comp.diffuse_indirect.Output
    mg = comp.AddTool("Merge", 1, 1)  # Create merge tool
    mg_foreground = comp.Merge1.ConnectInput("Foreground", diff_direct)
    mg_background = comp.Merge1.ConnectInput("Background", diff_indir)
    specul_direct = comp.specular_direct.Output  # get output of node
    specul_indir = comp.specular_indirect.Output
    mg = comp.AddTool("Merge", 1, 3)  # Create merge tool
    mg_foreground = comp.Merge2.ConnectInput("Foreground", specul_direct)
    mg_background = comp.Merge2.ConnectInput("Background", specul_indir)
    occ_out = comp.Occ.Output
    mg1_out = comp.Merge1.Output
    mg = comp.AddTool("Merge", 1, 5)
    mg_foreground = comp.Merge3.ConnectInput("Foreground", occ_out)
    mg_background = comp.Merge3.ConnectInput("Background", mg1_out)
    mg3_out = comp.Merge3.Output
    mg2_out = comp.Merge2.Output
    mg = comp.AddTool("Merge", 1, 7)
    mg_foreground = comp.Merge4.ConnectInput("Foreground", mg3_out)
    mg_background = comp.Merge4.ConnectInput("Background", mg2_out)
    trans_out = comp.transmission.Output
    transd_out = comp.transmission_direct.Output
    mg = comp.AddTool("Merge", 1, 8)
    mg_foreground = comp.Merge5.ConnectInput("Foreground", trans_out)
    mg_background = comp.Merge5.ConnectInput("Background", transd_out)
    mg4_out = comp.Merge4.Output
    mg5_out = comp.Merge5.Output
    mg = comp.AddTool("Merge", 1, 10)
    mg_foreground = comp.Merge6.ConnectInput("Foreground", mg5_out)
    mg_background = comp.Merge6.ConnectInput("Background", mg4_out)
    sssd_out = comp.sss_direct.Output
    sssid_out = comp.sss_indirect.Output
    mg = comp.AddTool("Merge", 1, 12)
    mg_foreground = comp.Merge7.ConnectInput("Foreground", sssd_out)
    mg_background = comp.Merge7.ConnectInput("Background", sssid_out)
    mg6_out = comp.Merge6.Output
    mg7_out = comp.Merge7.Output
    mg = comp.AddTool("Merge", 1, 14)
    mg_foreground = comp.Merge8.ConnectInput("Foreground", mg7_out)
    mg_background = comp.Merge8.ConnectInput("Background", mg6_out)
    # comp.SetActiveTool(comp.FindTool("Merge8"))
    at = comp.AddTool("ChannelBoolean", 3, 14)
    mg_out = comp.Merge8.Output
    lodr_out = comp.Loader1.Output
    at_foreground = comp.ChannelBooleans1.ConnectInput("Foreground", lodr_out)
    at_background = comp.ChannelBooleans1.ConnectInput("Background", mg_out)
    at = comp.AddTool("ChannelBoolean", 8, 15)
    mg_out = comp.ChannelBooleans1.Output
    lodr_out = comp.P.Output
    at_foreground = comp.ChannelBooleans2.ConnectInput("Foreground", lodr_out)
    at_background = comp.ChannelBooleans2.ConnectInput("Background", mg_out)
    vm = comp.AddTool("VolumeMask", 8, 16)
    mg_out = comp.ChannelBooleans2.Output
    vm_background = comp.VolumeMask1.ConnectInput("Image", mg_out)
    ad = comp.AddTool("AlphaDivide", 5.5, 15)
    mg_out = comp.ChannelBooleans1.Output
    ad_background = comp.AlphaDivide1.ConnectInput("Input", mg_out)
    act = comp.SetActiveTool(comp.FindTool("AlphaDivide1"))
    comp.Execute(
        "!Py2: comp.Paste(bmd.readfile(comp.MapPath('C:/ProgramData/Blackmagic Design/Fusion/Reactor/Deploy/Macros/Blur/DepthDefocus.setting'))) ")
    at = comp.AddTool("ChannelBoolean", 10, 18)
    mg_out = comp.ChannelBooleans1.Output
    lodr_out = comp.N.Output
    at_foreground = comp.ChannelBooleans3.ConnectInput("Foreground", lodr_out)
    at_background = comp.ChannelBooleans3.ConnectInput("Background", mg_out)
    at = comp.AddTool("Shader", 8, 18)
    mg_out = comp.ChannelBooleans3.Output
    at_foreground = comp.Shader1.ConnectInput("Input", mg_out)
    at = comp.AddTool("BitmapMask", 7, 18)
    mg_out = comp.Shader1.Output
    at_foreground = comp.Bitmap3.ConnectInput("Image", mg_out)
    bg = comp.AddTool("Background", 2, 25)
    bg = comp.AddTool("OCIOColorSpace", 4, 25)
    mg_out = comp.Background1.Output
    ad_background = comp.OCIOColorSpace1.ConnectInput("Input", mg_out)
    ad = comp.AddTool("ColorCorrector", 6, 18)
    ad = comp.AddTool("Fuse.Grade", 6, 20)
    mg_out = comp.ColorCorrector1.Output
    ad_background = comp.Grade1.ConnectInput("Input", mg_out)
    ad = comp.AddTool("AlphaMultiply", 6, 22)
    mg_out = comp.Grade1.Output
    ad_background = comp.AlphaMultiply1.ConnectInput("Input", mg_out)
    occ_out = comp.AlphaMultiply1.Output
    mg1_out = comp.OCIOColorSpace1.Output
    mg = comp.AddTool("Merge", 6, 25)
    mg_foreground = comp.Merge9.ConnectInput("Foreground", occ_out)
    mg_background = comp.Merge9.ConnectInput("Background", mg1_out)
    mg_out = comp.Bitmap3.Mask
    at_foreground = comp.ColorCorrector1.ConnectInput("EffectMask", mg_out)
    bg = comp.AddTool("OCIOColorSpace", 8, 25)
    mg_out = comp.Merge9.Output
    ad_background = comp.OCIOColorSpace2.ConnectInput("Input", mg_out)
    comp.DepthDefocus.Input = comp.AlphaDivide1.Output
    comp.PipeRouter4.Input = comp.AlphaDivide1.Output
    comp.DepthDefocus.Input = comp.AlphaDivide1.Output
    comp.ColorCorrector1.Input = comp.DepthDefocus.Output
    comp.AddTool("FileLUT", 9, 25)
    comp.FileLUT1.Input = comp.OCIOColorSpace2.Output
    comp.SetActiveTool(comp.FindTool("sss"))
    ActTool = comp.ActiveTool
    comp.Copy(ActTool)
    comp.CurrentFrame.FlowView.Select(11, 7)
    comp.Paste()
    comp.sss_1.SetAttrs({'TOOLS_Name': "Z"})
    comp.SetActiveTool(comp.FindTool("Z"))
    ActTool = comp.ActiveTool
    flow.SetPos(ActTool, 11, 7)
    comp.AddTool("Custom", 9, 7)
    comp.CustomTool1.Image1 = comp.Z.Output
    ActTool.Clip1.OpenEXRFormat.RedName = 'Z'
    ActTool.Clip1.OpenEXRFormat.GreenName = 'Z'
    ActTool.Clip1.OpenEXRFormat.BlueName = 'Z'
    ActTool.Clip1.OpenEXRFormat.AlphaName = 'Z'
    comp.DepthDefocus.DepthMap = comp.CustomTool1.Output
    return


def positn():
    global flow
    comp.Lock()
    flow = comp.CurrentFrame.FlowView
    comp.SetActiveTool(comp.FindTool("diffuse_indirect"))
    ActTool = comp.ActiveTool
    flow.SetPos(ActTool, 2, 1)
    comp.SetActiveTool(comp.FindTool("Merge1"))
    ActTool = comp.ActiveTool
    flow.SetPos(ActTool, 3, 2)
    comp.SetActiveTool(comp.FindTool("diffuse_direct"))
    ActTool = comp.ActiveTool
    flow.SetPos(ActTool, 2, 2)
    comp.SetActiveTool(comp.FindTool("OCC"))
    ActTool = comp.ActiveTool
    flow.SetPos(ActTool, 2, 4)
    comp.SetActiveTool(comp.FindTool("Merge3"))
    ActTool = comp.ActiveTool
    flow.SetPos(ActTool, 5, 4)
    comp.SetActiveTool(comp.FindTool("Specular_indirect"))
    ActTool = comp.ActiveTool
    flow.SetPos(ActTool, 2, 5)
    comp.SetActiveTool(comp.FindTool("Specular_direct"))
    ActTool = comp.ActiveTool
    flow.SetPos(ActTool, 2, 6)
    comp.SetActiveTool(comp.FindTool("Merge2"))
    ActTool = comp.ActiveTool
    flow.SetPos(ActTool, 3, 6)
    comp.SetActiveTool(comp.FindTool("Merge4"))
    ActTool = comp.ActiveTool
    flow.SetPos(ActTool, 5, 6)
    comp.SetActiveTool(comp.FindTool("transmission"))
    ActTool = comp.ActiveTool
    flow.SetPos(ActTool, 2, 7)
    comp.SetActiveTool(comp.FindTool("transmission_direct"))
    ActTool = comp.ActiveTool
    flow.SetPos(ActTool, 2, 8)
    comp.SetActiveTool(comp.FindTool("Merge5"))
    ActTool = comp.ActiveTool
    flow.SetPos(ActTool, 3, 7)
    comp.SetActiveTool(comp.FindTool("Merge6"))
    ActTool = comp.ActiveTool
    flow.SetPos(ActTool, 5, 8)
    comp.SetActiveTool(comp.FindTool("sss_direct"))
    ActTool = comp.ActiveTool
    flow.SetPos(ActTool, 2, 10)
    comp.SetActiveTool(comp.FindTool("sss_indirect"))
    ActTool = comp.ActiveTool
    flow.SetPos(ActTool, 2, 9)
    comp.SetActiveTool(comp.FindTool("Merge7"))
    ActTool = comp.ActiveTool
    flow.SetPos(ActTool, 3, 10)
    comp.SetActiveTool(comp.FindTool("Merge8"))
    ActTool = comp.ActiveTool
    flow.SetPos(ActTool, 5, 10)
    comp.SetActiveTool(comp.FindTool("ChannelBooleans1"))
    ActTool = comp.ActiveTool
    flow.SetPos(ActTool, 5, 12)
    comp.SetActiveTool(comp.FindTool("Loader1"))
    ActTool = comp.ActiveTool
    flow.SetPos(ActTool, 7, 1)
    comp.SetActiveTool(comp.FindTool("P"))
    ActTool = comp.ActiveTool
    flow.SetPos(ActTool, 11, 9)
    comp.SetActiveTool(comp.FindTool("N"))
    ActTool = comp.ActiveTool
    flow.SetPos(ActTool, 11, 11)
    comp.SetActiveTool(comp.FindTool("DepthDefocus"))
    ActTool = comp.ActiveTool
    flow.SetPos(ActTool, 5, 16)
    comp.Unlock()
    return


def rename():
    global flow
    comp.ChannelBooleans1.SetAttrs({'TOOLS_Name': "alpha_copy"})
    comp.ChannelBooleans2.SetAttrs({'TOOLS_Name': "position_pass"})
    comp.ChannelBooleans3.SetAttrs({'TOOLS_Name': "normalpass"})
    comp.ColorCorrector1.SetAttrs({'TOOLS_Name': "Relighting_CC"})
    comp.Background1.SetAttrs({'TOOLS_Name': "BG_INPUT"})
    comp.AddTool("Note", 6, 5.8)
    comp.Note1.Comments = "Adjust Occlusion blend value as per your need"
    comp.Note1.SetAttrs({'TOOLS_Name': "Occlusion"})
    comp.AddTool("Note", 6, 10.5)
    comp.Note1.Comments = "Blend opacity of your choice"
    comp.Note1.SetAttrs({'TOOLS_Name': "Merg8"})
    comp.AddTool("Note", 4, 15.5)
    comp.Note1.Comments = "Use this if necessary or use frishluft lens defocus"
    comp.Note1.SetAttrs({'TOOLS_Name': "DepthDeFocus Z"})
    comp.AddTool("Note", 2, 23)
    comp.Note1.Comments = "Replace with your inputs, make sure to work in 32BIT workflow"
    comp.Note1.SetAttrs({'TOOLS_Name': "Input32Bit"})
    comp.CustomTool1.SetAttrs({'TOOLS_Name': "Z_CustomDivide"})
    comp.CurrentFrame.FlowView.Select()
    return


def small_exr():
    global flow
    comp.SetActiveTool(comp.FindTool("sss_direct"))
    ActTool = comp.ActiveTool
    comp.Copy(ActTool)
    comp.CurrentFrame.FlowView.Select()
    comp.Paste()
    comp.SetActiveTool(comp.FindTool("sss_indirect"))
    ActTool = comp.ActiveTool
    comp.Copy(ActTool)
    comp.CurrentFrame.FlowView.Select()
    comp.Paste()
    inputtools = comp.GetToolList()
    for i in inputtools:
        name = inputtools[i].GetAttrs('TOOLS_Name')
        if name == 'sss_direct_1':
            flow.SetPos(inputtools[i], 15, -3)
            sss_direct_1 = comp.sss_direct_1.output
        if name == 'sss_indirect_1':
            flow.SetPos(inputtools[i], 15, -5)
            sss_indirect_1 = comp.sss_indirect_1.output
        if name == 'sss_albedo':
            flow.SetPos(inputtools[i], 15, -1)
            sss_albedo = comp.sss_albedo.output
    comp.AddTool('Merge', 17, -2)
    comp.Merge1.ConnectInput("Foreground", sss_direct_1)
    comp.Merge1.ConnectInput("Background", sss_indirect_1)
    comp.Merge1.SetAttrs({'TOOLS_Name': 'Merge7_1'})
    comp.AddTool('ChannelBoolean', 17, 0)
    comp.ChannelBooleans1.ConnectInput("Foreground", sss_albedo)
    comp.ChannelBooleans1.ConnectInput("Background", comp.Merge7_1.Output)
    comp.ChannelBooleans1.SetAttrs({'TOOLS_Name': 'divide'})
    comp.AddTool('Fuse.Grade', 17, 2)
    comp.Grade1.Input = comp.divide.Output
    comp.Grade1.SetAttrs({'TOOLS_Name': 'Grade3'})
    comp.AddTool('ChannelBoolean', 17, 4)
    comp.ChannelBooleans1.ConnectInput("Foreground", sss_albedo)
    comp.ChannelBooleans1.ConnectInput("Background", comp.Grade3.Output)
    comp.ChannelBooleans1.SetAttrs({'TOOLS_Name': 'multiply'})
    comp.AddTool("Note", 15, 0)
    comp.Note1.SetAttrs({"TOOLS_Name": 'albedo_workflow'})
    return


def controls():
    global flow
    # comp.Merge1.Blend = 0.6
    comp.Merge1.Gain = 0
    # comp.Merge2.Blend = 0.6
    comp.Merge2.Gain = 0
    # comp.Merge3.Blend = 0.6
    comp.Merge3.Gain = 0
    comp.Merge3.ApplyMode = "Multiply"
    comp.Merge3.PerformDepthMerge = 0
    # comp.Merge4.Blend = 0.6
    comp.Merge4.Gain = 0
    # comp.Merge5.Blend = 0.6
    comp.Merge5.Gain = 0
    # comp.Merge6.Blend = 0.6
    comp.Merge6.Gain = 0
    # comp.Merge7.Blend = 0.6
    comp.Merge7.Gain = 0
    # comp.Merge7_1.Blend = 0.6
    comp.Merge7_1.Gain = 0
    # comp.Merge8.Blend = 0.6
    comp.Merge8.Gain = 0
    comp.alpha_copy.ToRed = 4
    comp.alpha_copy.ToGreen = 4
    comp.alpha_copy.ToBlue = 4
    comp.position_pass.ToRed = 4
    comp.position_pass.ToGreen = 4
    comp.position_pass.ToBlue = 4
    comp.position_pass.ToAlpha = 4
    comp.normalpass.ToRed = 4
    comp.normalpass.ToGreen = 4
    comp.normalpass.ToBlue = 4
    comp.normalpass.ToAlpha = 4
    comp.BG_INPUT.TopLeftRed = 0.04
    comp.BG_INPUT.TopLeftGreen = 0.04
    comp.BG_INPUT.TopLeftBlue = 0.04
    comp.Grade1.Offset_Red = 0.05657958984375
    comp.Grade1.Offset_Green = 0.040191650390625
    comp.Grade1.Offset_Blue = 0.02911376953125
    comp.Grade1.BlackClamp = 0
    comp.Grade3.Mult_Red = 0.19
    comp.Grade3.Mult_Green = 2.88
    comp.Grade3.Mult_Blue = 4
    comp.OCIOColorSpace1.OCIOConfig = "\\\\san\\06_LIBRARY\\12_SCRIPTS_AND_WORKFILES\\common\\OpenColorIO-Configs-master\\aces_1.0.3\\pfx_config.ocio"
    comp.OCIOColorSpace1.SourceSpace = "Input - ARRI - Curve - V3 LogC (EI800)"
    comp.OCIOColorSpace1.OutputSpace = "ACES - ACEScg"
    comp.OCIOColorSpace1.Look = "None"
    comp.OCIOColorSpace2.OCIOConfig = "\\\\san\\06_LIBRARY\\12_SCRIPTS_AND_WORKFILES\\common\\OpenColorIO-Configs-master\\aces_1.0.3\\pfx_config.ocio"
    comp.OCIOColorSpace2.SourceSpace = "ACES - ACEScg"
    comp.OCIOColorSpace2.OutputSpace = "Input - ARRI - Curve - V3 LogC (EI800)"
    comp.OCIOColorSpace2.Look = "None"
    comp.multiply.Operation = 6
    comp.divide.Operation = 7
    comp.Bitmap3.MaskWidth = 1920
    comp.Bitmap3.MaskHeight = 1080
    comp.Bitmap3.PixelAspect = 1, 1
    comp.Bitmap3.ClippingMode = "None"
    comp.Bitmap3.Channel = "Luminance"
    comp.Shader1.EquatorAngle = -56.1
    return


def main():
    global flow
    result = ''
    flow = comp.CurrentFrame.FlowView
    ActTool = comp.ActiveTool
    flow.SetPos(ActTool, 0, 0)
    hosSplit()
    sleep(5)
    small_exr()
    addtool()
    mrge()
    positn()
    rename()
    controls()
    exit()


main()