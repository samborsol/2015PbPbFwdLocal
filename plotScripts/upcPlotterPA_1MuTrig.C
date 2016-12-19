void upcPlotterPA_1MuTrig(){

	TChain *t = new TChain("hltMuTree/HLTMuTree");
	TChain *t2 = new TChain("hltanalysis/HltTree");
	t->Add("taskManagement/crab_Hiforest_PbPb_Run2015_mltMu_v20/results/*.root");
	t2->Add("taskManagement/crab_Hiforest_PbPb_Run2015_mltMu_v20/results/*.root");

	t->AddFriend(t2);

	Int_t bins = 30;
	Float_t minB = 8.5;
	Float_t maxB = 10.5;

	TH1F *h1 = new TH1F("h1","h1",bins,minB,maxB);

	//TCut rapCut= "(Di_rapidity<-1.8&&Di_rapidity>-2.4)||(Di_rapidity<2.4&&Di_rapidity>1.8)||(Di_rapidity>-0.5&&Di_rapidity<0.5)";
	TCut rapCut = "Di_rapidity<1 && Di_rapidity>-1";
	TCut ptCut = "Di_pt<1.5";
	//TCut trig1 = "HLT_HIUPCL1DoubleMuOpenNotHF2_v1";
	TCut trig1 = "HLT_HIUPCDoubleMuNotHF2Pixel_SingleTrack_v1";
	TCut massCut="Di_mass>9.43 && Di_mass<9.48";
	t->Draw("Di_mass >> h1",trig1+ptCut);


	TCanvas *c1 = new TCanvas("c1","hists with different scales",700,700);
	gStyle->SetOptStat(kFALSE);

	h1->SetTitle("Dimuon Inv. Mass, (pt < 1.5 GeV/c)");
	h1->GetXaxis()->SetTitle("Mass (GeV/c^2)");
	h1->GetYaxis()->SetTitle("Events /bin");
	h1->SetLineColor(kBlue);
	h1->SetLineWidth(1);
	h1->GetYaxis()->SetLabelSize(0.03);
	h1->GetYaxis()->SetTitleOffset(1.50);

	TLegend *leg = new TLegend(0.1,0.85,0.75,0.9);
	leg->SetFillStyle(0);
	leg->SetTextSize(0.025);
   	leg->AddEntry(h1,"HLT_HIUPCL1DoubleMuOpenNotHF2_v1","l");

	h1->Draw();
	//leg->Draw("same");
	c1->Update();
}
