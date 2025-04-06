import { Component } from '@angular/core';
import { FormControl, FormsModule } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { ApiService } from '../../services/api.service';
import { CommonModule } from '@angular/common';
import { GoogleMapsModule, MapDirectionsService } from '@angular/google-maps';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-plantrip',
  standalone: true,
  providers: [ApiService],
  imports: [
    ReactiveFormsModule,
    FormsModule,
    CommonModule,
    GoogleMapsModule
  ],
  templateUrl: './plantrip.component.html',
  styleUrl: './plantrip.component.css'
})

export class PlantripComponent {
  whereto: FormControl = new FormControl('los angeles');
  budget: FormControl = new FormControl(200);
  itinerary: any = {};
  title: string = 'title';

  center = { lat: 40.712776, lng: -74.005974 };
  zoom = 15;
  directionsResults?: google.maps.DirectionsResult;

  constructor(private _apiservice: ApiService, private _http: HttpClient) {}

  getTrip(whereto: string, budget: number) {
    this._apiservice.getCalc(this.whereto.value, this.budget.value).subscribe(res => {
      this.itinerary = res;
      console.log(this.itinerary);
    });
  }

  objectKeys(obj: any) {
    return Object.keys(obj);
  }
}
