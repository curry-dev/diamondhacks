import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor() { }
  // constructor(private _http: HttpClient) { }

  // getCalc(from: string, to: string) {
  //   return this._http.post<{ response: string, chosen_city: string[] }>('http://localhost:4200/calculate', { from: from, to: to });
  // }
}
