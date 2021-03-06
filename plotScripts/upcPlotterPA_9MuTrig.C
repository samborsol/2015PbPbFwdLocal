#include "TChain.h"
#include "TH1F.h"
#include "TCut.h"
#include "TCanvas.h"
#include "TLegend.h"
#include "TStyle.h"

void upcPlotterPA_9MuTrig(){


	Int_t bins = 50;
	Double_t minB = -4;
	Double_t maxB = 4;

	TH1F *h1 = new TH1F("h1","h1",bins,minB,maxB);
	TH1F *h2 = new TH1F("h2","h2",bins,minB,maxB);
	TH1F *h3 = new TH1F("h3","h3",bins,minB,maxB);
	TH1F *h4 = new TH1F("h4","h4",bins,minB,maxB);
	TH1F *h5 = new TH1F("h5","h5",bins,minB,maxB);
	TH1F *h6 = new TH1F("h6","h6",bins,minB,maxB);

	TCut ptCut = "Di_pt<1.5";
        TCut rapCut = "(Di_rapidity<2.3)||(Di_rapidity>-2.3)";
	TCut massCut = "Di_mass<9.55 && Di_mass>9.35";

	TCut trig1 = "HLT_PADoubleMuOpen_HFTwoTowerVeto_v1";
	TCut trig2 = "HLT_PADoubleMuOpen_HFTwoTowerVeto_SingleTrack_v1";
	TCut trig3 = "HLT_PASingleMuOpen_PixelTrackGt0Lt15_v1";
	TCut trig4 = "HLT_PASingleMuOpen_PixelTrackGt0_FullTrackLt15_v1";
	TCut trig5 = "HLT_PASingleMuOpen_PixelTrackGt0Lt10_v1";
	TCut trig6 = "HLT_PASingleMuOpen_PixelTrackGt0_FullTrackLt10_v1";

        TFile *f1 = new TFile("trigger_pA2016CMu.root");
        TFile *f2 = new TFile("dimu_pA2016CMu.root");
        TFile *f3 = new TFile("hiHF_pA2016CMu.root");

        TTree *t = (TTree*)f1->Get("HLTMuTree");
        TTree *t2 = (TTree*)f2->Get("HltTree");
        TTree *t3 = (TTree*)f3->Get("HiTree");

        t->AddFriend(t2);
	t->AddFriend(t3);

        h1->GetDirectory()->cd();
        h2->GetDirectory()->cd();
        h3->GetDirectory()->cd();
        h4->GetDirectory()->cd();
        h5->GetDirectory()->cd();
        h6->GetDirectory()->cd();

	t->Draw("Di_rapidity >> h1",trig1+ptCut+massCut);
	t->Draw("Di_rapidity >> h2",trig2+ptCut+massCut);
	//t->Draw("Di_pt >> h3",trig3+rapCut+massCut);
	//t->Draw("Di_pt >> h4",trig4+rapCut+massCut);
	//t->Draw("Di_pt >> h5",trig5+rapCut+massCut);
	//t->Draw("Di_pt >> h6",trig6+rapCut+massCut);

	TCanvas *c1 = new TCanvas("c1","hists with different scales",700,700);
	gStyle->SetOptStat(kFALSE);

	h1->SetTitle("Dimuon Rapidity (Upsilon)");
	h1->GetXaxis()->SetTitle("Rapidity (y)");
	h1->GetYaxis()->SetTitle("Events /bin");
	h1->SetLineColor(kBlue);
	h1->SetLineWidth(1);
	h1->GetYaxis()->SetLabelSize(0.03);
	h1->GetYaxis()->SetTitleOffset(1.50);
	//h1->SetMaximum(600);
	//h1->SetMinimum(0);

	h2->SetLineColor(kRed);
	h3->SetLineColor(kGreen);
	h4->SetLineColor(kBlue);
	h4->SetLineStyle(2);
	h5->SetLineColor(kRed);
	h5->SetLineStyle(2);
	h6->SetLineColor(kGreen);
	h6->SetLineStyle(2);
	h6->SetLineWidth(2);


	TLegend *leg = new TLegend(0.1,0.80,0.90,0.9);
	leg->SetFillStyle(0);
	leg->SetTextSize(0.025);
	leg->AddEntry(h1,"HLT_PADoubleMuOpen_HFTwoTowerVeto_v1","l");
	leg->AddEntry(h2,"HLT_PADoubleMuOpen_HFTwoTowerVeto_SingleTrack_v1","l");
	//leg->AddEntry(h3,"HLT_PASingleMuOpen_PixelTrackGt0Lt15_v1","l");
	//leg->AddEntry(h4,"HLT_PASingleMuOpen_PixelTrackGt0_FullTrackLt15_v1","l");
	//leg->AddEntry(h5,"HLT_PASingleMuOpen_PixelTrackGt0Lt10_v1","l");
	//leg->AddEntry(h6,"HLT_PASingleMuOpen_PixelTrackGt0_FullTrackLt10_v1","l");

	h1->Draw();
	h2->Draw("same");
	//h3->Draw("same");
	//h4->Draw("same");
	//h5->Draw("same");
	//h6->Draw("same");
	leg->Draw("same"); 
	c1->Update();

}
