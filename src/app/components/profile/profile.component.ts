import { Component } from '@angular/core';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-profile',
  standalone: true,
  imports: [],
  templateUrl: './profile.component.html',
  styleUrl: './profile.component.css'
})
export class ProfileComponent {
  user: any;

  constructor(private _api: ApiService) { }

  getUser() {
    return this._api.getUser().subscribe((response) => {
      this.user = response;
      console.log('user =', this.user);
    });
  }

  ngOnInit() {
    this.getUser();
  }
}
