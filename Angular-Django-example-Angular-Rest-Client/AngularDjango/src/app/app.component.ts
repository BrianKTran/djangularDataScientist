import { Component } from '@angular/core';



@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'DjAngular Analytical Solution';
  description = ' Postgres Database - Angular Client - Django Server - Pandas ';
  csvoutput = 'Download List in CSV';



  // downloadFile(name){
  //   this.connectorsService.downloadFile(name).subscribe(
  //   res => {this.successDownloadFile(res, name);},
  //   error =>  this.errorMessage = <any>error,
  //   ()=> {});
  // }
  //
  // successDownloadFile(res: any, name: String){
  //
  //  this.showLoader = false;
  //  let blob;
  //
  //  blob = new Blob([res._body], {type: 'application/vnd.ms-excel'});
  //
  //  FileSaver.saveAs(blob, name.toString());
  // }



}
