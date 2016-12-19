void upcPlotterPA_3MuTrig(){

 	TFile *f = new TFile("pA2016C_Mu.root");
	TTree *t = (TTree*)f->Get("hltMuTree/HLTMuTree");
	TTree *t2= (TTree*)f->Get("hltanalysis/HltTree");
	t->AddFriend(t2);

	Int_t bins = 600;
	Double_t minB = -4;
	Double_t maxB = 4;

	TH1F *h1 = new TH1F("h1","h1",bins,minB,maxB);

	TCut ptCut = "Di_pt<1.5";
        TCut trig1 = "HLT_PASingleMuOpen_HFTwoTowerVeto_v1";
//	TCut rapCut = "(Di_rapidity<2.2&&Di_rapidity>1.8)||(Di_rapidity>-2.2&&Di_rapidity<-1.8)";
	TCut massCut = "Di_mass>9.4 && Di_mass<9.5";


	t->Draw("Di_rapidity >> h1",trig1+ptCut+massCut);

	TCanvas *c1 = new TCanvas("c1","hists with different scales",700,700);
	gStyle->SetOptStat(kFALSE);

	h1->SetTitle("Dimuon Rapidity");
	h1->GetXaxis()->SetTitle("Rapidity, y");
	h1->GetYaxis()->SetTitle("Events /bin");
	h1->SetLineColor(kBlue);
	h1->SetLineWidth(1);
//	h1->SetMaximum(80);
	h1->GetYaxis()->SetLabelSize(0.03);
	h1->GetYaxis()->SetTitleOffset(1.50);

	TLegend *leg = new TLegend(0.1,0.85,0.75,0.9);
	leg->SetFillStyle(0);
	leg->SetTextSize(0.025);
   	leg->AddEntry(h1,"HLT_PASingleMuOpen_HFTwoTowerVeto_v1","l");

	h1->Draw();
	leg->Draw("same");
	c1->Update();
}
