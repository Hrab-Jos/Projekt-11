import React, {useState} from 'react'
import Modal from 'react-modal';
import Moment from 'moment';

Modal.setAppElement('#modal');
Moment.locale('cs');

const Main = ({notifications, userid}) => {
	const [openedItem, setOpenedItem] = useState(null)
	const [data, setData] = useState(null)

	const onNotificationClick = (id) => {
		fetch(`/notification/${id}`).then(x => x.json()).then(jsonData => setData(jsonData))
		setOpenedItem(id)
	}

	const closeModal = () => {
		setOpenedItem(null);
		setData(null);
	}

	const onSeenClick = (id, userid) => {
		fetch(`/notification/${id}/mark-user-seen/${userid}`, {
			method: 'POST'
		}).then(resp => {
			if (resp.ok) {
				closeModal()
			}
		})
	}				

	return (
		<div>
		<ul>
		{notifications.map(x=> <li>
			<a onClick={() => onNotificationClick(x.id)}>{x.header} - {x.datetime}</a>
		</li>)}
		</ul>
		<Modal
        isOpen={data !== null}
        onRequestClose={closeModal}
        contentLabel="Example Modal"
      >
      	<h2>{data?.header} - {Moment(data?.date).format('DD.MM.YYYY H:MM')}</h2>
      	<p>{data?.message}</p>
      	<ul>
      		{data?.users.map(x => <li>{x}</li>)}
      	</ul>
      	<button onClick={() => onSeenClick(data?.id, userid)}>Viděno</button>
        <button onClick={closeModal}>close</button>
      </Modal>
 		</div>
	)
}

export default Main